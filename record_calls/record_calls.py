
# %% Import 
from functools import wraps

# %%

NO_RETURN = object()

class Call:
    """ Results of a function call """
    def __init__(self, args, kwargs, return_value=NO_RETURN, exception=None):
        self.args = args
        self.kwargs = kwargs
        self.return_value = return_value
        self.exception = exception


def record_calls(func):
    """ Record the number of function calls """
    @wraps(func)
    def call_tracking(*args, **kwargs):
        # call function
        try:
            return_value = func(*args, **kwargs)
        except Exception as original_exception:
            exception = original_exception
            return_value = NO_RETURN
        else:
            exception = None

        # track
        call_tracking.call_count += 1
        call_tracking.calls.append(
            Call(
                args,
                kwargs,
                return_value=return_value,
                exception=exception,
            )
        )

        # result of function
        if exception is not None:
            raise exception
        return return_value

    # initialize
    call_tracking.call_count = 0
    call_tracking.calls = []
    return call_tracking

# %% Example use cases

@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")

@record_calls
def cube(n):
    return n**3

# %%
if __name__ == "__main__":
    for i in range(5):
        greet(f'yo{i}')
        print(f'call count {greet.call_count}')
        print(f'calls {len(greet.calls)}')
        print(f'last call {greet.calls[-1].args}')
    greet(None)

    cube(3)
    cube(None)

# %%
