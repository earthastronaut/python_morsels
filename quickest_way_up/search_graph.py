
# %%
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
    stack = [(start, [start])]
    pop_from = -1 if depth_first else 0

    while len(stack):

        node, path = stack.pop(pop_from)

        logger.debug(f'Path: {path}')
        if callback is not None:
            goal_achieved = callback(path)
            if goal_achieved:
                return path

        children = get_children(node) or []
        for child in children:
            if child in path:
                continue
            stack.append((child, path + [child]))


# %%
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    graph={
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E',],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F', 'G'],
        'F': ['C', 'E'],
    }

    result = search_graph('B', graph.get, depth_first=True)

# %%
