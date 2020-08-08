# %%
from functools import wraps
# %%

class suppress:
    """ Suppress exceptions of a given type """

    def __init__(self, *suppress_exceptions):
        self.suppress_exceptions = suppress_exceptions
        self.exception = None
        self.traceback = None

    def __call__(self, func):
        func.suppressed = self
        @wraps(func)
        def suppress_exceptions(*args, **kws):
            with self:
                return func(*args, **kws)
        return suppress_exceptions

    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception, traceback):
        self.exception = exception
        self.traceback = traceback
        return isinstance(self.exception, self.suppress_exceptions)

# %%

@suppress(ValueError)
def tester():
    raise ValueError('blah')

if __name__ == "__main__":
    with suppress(KeyError, TypeError) as ctx:
        # x = int('hello')
        yo = {}
        yo['hello']

    tester()
