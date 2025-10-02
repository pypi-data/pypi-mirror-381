import inspect
import threading
import re
import textwrap


def get_full_name(fn):
    return f"{fn.__module__}.{fn.__qualname__}"

class JITCallable:

    def __init__(self, fn):
        self.fn = fn
        self.signature = inspect.signature(fn)
        try:
            self.raw_src, self.starting_line_number = inspect.getsourcelines(fn)
        except OSError as e:
            raise ValueError("@jit functions should be defined in a Python file") from e
        self._fn_name = get_full_name(fn)
        self._hash_lock = threading.RLock()

        # function source code (without decorators)
        src = textwrap.dedent("".join(self.raw_src))
        src = src[re.search(r"^def\s+\w+\s*\(", src, re.MULTILINE).start():]
        self._src = src
        self.hash = None

        # Map of global variables used by the function and any functions it
        # transitively calls, plus their values.  The values are collected when
        # the function is first compiled.  Then every time we run the function,
        # we check that the values of the globals match what's expected,
        # otherwise we raise an error.
        #
        # Different functions can have different __globals__ maps, so the map
        # key is actually (var name, id(__globals__)), and the map value is
        # (value, __globals__).
        self.used_global_vals: Dict[Tuple[str, int], Tuple[Any, Dict[str, Any]]] = {}

        # reuse docs of wrapped function
        self.__doc__ = fn.__doc__
        self.__name__ = fn.__name__
        self.__qualname__ = fn.__qualname__
        self.__globals__ = fn.__globals__
        self.__module__ = fn.__module__

    def get_capture_scope(self):
        return self.__globals__ | inspect.getclosurevars(self.fn).nonlocals

    @property
    def cache_key(self):
        # TODO : hash should be attribute of `self`
        with self._hash_lock:
            if self.hash is not None:
                return self.hash
            # Set a placeholder hash to break recursion in case the function
            # transitively calls itself. The full hash is set after.
            self.hash = f"recursion:{self._fn_name}"
            nonlocals = inspect.getclosurevars(self.fn).nonlocals
            dependencies_finder = DependenciesFinder(name=self._fn_name, globals=self.__globals__, nonlocals=nonlocals,
                                                     src=self.src)
            dependencies_finder.visit(self.parse())
            self.hash = dependencies_finder.ret + str(self.starting_line_number)
            self.used_global_vals = dict(sorted(dependencies_finder.used_global_vals.items()))

            from triton.language.core import constexpr
            self.hash += str([(name, val)
                              for (name, _), (val, _) in self.used_global_vals.items()
                              if isinstance(val, constexpr)])
            self.hash = hashlib.sha256(self.hash.encode("utf-8")).hexdigest()
        return self.hash

    # we do not parse `src` in the constructor because
    # the user might want to monkey-patch self.src dynamically.
    # Our unit tests do this, for example.
    def parse(self):
        tree = ast.parse(self._src)
        assert isinstance(tree, ast.Module)
        assert len(tree.body) == 1
        assert isinstance(tree.body[0], ast.FunctionDef)
        return tree

    @property
    def type(self):
        from triton.language.core import constexpr_type
        return constexpr_type(self)

    def _unsafe_update_src(self, new_src):
        """
        The only method allowed to modify src.
        Bypasses the __setattr__ restriction by calling super().__setattr__ directly.

        Note that it is the callers responsibility to make sure any triton functions that call this function have the `.hash` value reset to None.
        """
        self.hash = None
        self._src = new_src

    def _set_src(self):
        raise AttributeError("Cannot set attribute 'src' directly. "
                             "Use '_unsafe_update_src()' and manually clear `.hash` of all callers"
                             "instead.")

    def _get_src(self):
        return self._src

    src = property(fget=_get_src, fset=_set_src)

class ConstexprFunction(JITCallable):

    def __init__(self, fn):
        super().__init__(fn)

    def __get__(self, obj, objclass):
        # Create a bound function to support constexpr_function methods
        if obj is not None:
            return BoundConstexprFunction(obj, self)
        return self

    def __call__(self, *args, _semantic=None, **kwargs):
        from triton.language.core import _unwrap_if_constexpr, constexpr
        # de-constexpr arguments and discard the _semantic keyword argument:
        args = [_unwrap_if_constexpr(x) for x in args]
        kwargs = {k: _unwrap_if_constexpr(v) for (k, v) in kwargs.items()}

        # call the raw Python function f:
        res = self.fn(*args, **kwargs)

        if _semantic is None:
            # Not called by triton code generator, e.g. in host code, another constexpr function, or even an aggreate's __init__ function
            return res

        # convert result back to a Triton constexpr:
        if knobs.runtime.interpret:
            return res  # No constexpr in interpreter
        return constexpr(res)


def constexpr_function(fn):
    """
    Wraps an arbitrary Python function so that it can be called at
    compile-time on constexpr arguments in a Triton function and
    returns a constexpr result.
    """
    return ConstexprFunction(fn)
