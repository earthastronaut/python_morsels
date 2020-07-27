# %%
from collections.abc import Iterable

# %%
def deep_flatten(iterable):
    """ Flatten iterable """
    for element in iterable:
        if isinstance(element, str):
            yield element
        elif isinstance(element, Iterable):
            for e in deep_flatten(element):
                yield e
        else:
            yield element
