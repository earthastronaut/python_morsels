
# %%
from collections import deque, namedtuple
import logging 
from typing import Dict, List, Hashable, Iterable, Callable, Union

logger = logging.getLogger(__name__)


def search_graph(
        start: Hashable,
        get_children: Callable[[Hashable], Union[Iterable, None]],
        callback: Callable[[List[Hashable]], bool] = None,
        depth_first: bool = True,
):
    """ Graph search function avoiding cicular patterns.

    Parameters
        start: Node (aka key) in the graph (aka dict)
        get_children: Returns children nodes in the graph. If graph is
            a dictionary of node keys and list of children. Then provide
            `get_children=graph.get`. 
        callback: If provided, calls `callback(path)` for 
            each path in the graph. If this returns True then
            the goal was achieved and it stops searching.
        depth_first: If True then does a depth first search 
            otherwise it's dreath first 

    Returns
        None or List[Hashable]: Returns None or the current path when
            `callable(path) == True`.
    """
    stack = deque()
    stack.append((start, [start], {start}))
    pop_node = stack.pop if depth_first else stack.popleft

    while len(stack):
        node, path, path_lookup = pop_node()

        # logger.debug(f'Path: {path}')
        if callback is not None:
            if callback(path):
                return path

        children = get_children(node) or tuple()
        for child in children:
            if child in path_lookup:
                continue
            stack.append((child, path + [child], path_lookup.union({child})))



# %%
if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    graph={
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E',],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F', 'G'],
        'F': ['C', 'E'],
    }

    result = search_graph('B', graph.get, depth_first=True)
    
    graph={
        0: {
            1: 4,
            7: 8,
        },
        1: {
            2: 8,
            7: 11,
        },
        2: {
            3: 7,
            5: 4,
            8: 2,
        },
        3: {
            4: 9,
            5: 14,
        },
        4: {
            5: 10,
        },
        5: {
            6: 2,
        },
        6: {
            8: 6,
            7: 1,
        },
        7: {
            8: 7,
        },
        8: {}
    }
    # weighted graph. Second dictionary gives the weight values.


# %%
