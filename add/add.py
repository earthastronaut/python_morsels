# %%

import itertools

# %%

def get_shape(list_matrix, index=None):
    if index is None:
        index = []

    length = len(list_matrix)
    shape = [length]

    next_level_shape = None
    for i, element in enumerate(list_matrix):
        if isinstance(element, list):
            element_index = index + [i]
            element_shape = get_shape(element, index=element_index)
            if next_level_shape is None:
                next_level_shape = element_shape
            elif element_shape != next_level_shape:
                raise ValueError(
                    f'Incorrect shape at list_matix{element_index}, shape {next_level_shape} != {element_shape}')
    shape.extend(next_level_shape or [])
    return shape


# %%

def create_empty_matrix(shape):
    """ Create empty list matrix for shape """
    result = []
    for _ in range(shape[0]):
        if len(shape) > 1:
            new = create_empty_matrix(shape[1:])
        else:
            new = []
        result.append(new)
    return result


def get_element(matrix, index):
    """ Access a deep element within the matrix by an index """
    sub_matrix = matrix
    for i in index:
        sub_matrix = sub_matrix[i]
    return sub_matrix


def append_element(matrix, index, element):
    """ Append an element deep into the matrix """
    leaf_matrix = matrix
    for i in index[:-1]:
        try:
            leaf_matrix = leaf_matrix[i]
        except IndexError:
            shape = get_shape(matrix)
            raise IndexError(f'Index={index} out of range for shape={shape}')
    leaf_matrix.append(element)


def set_element(matrix, index, element, operator=None):
    """ Set (or update) an element deep within the matrix """
    if not len(index):
        return
    operator = operator or (lambda a, b: b)
    leaf_matrix = matrix
    for i in index[:-1]:
        try:
            leaf_matrix = leaf_matrix[i]
        except IndexError:
            shape = get_shape(matrix)
            raise IndexError(f'Index={index} out of range for shape={shape}')
    i = index[-1]
    leaf_matrix[i] = operator(leaf_matrix[i], element)


def iter_index(shape):
    """ Loop over every index in the matrix shape """
    return itertools.product(*(
        range(length) for length in shape
    ))


# %%

def add(*lists):
    """ Elementwise addition of lists with the same shape """
    operator = lambda a, b: a + b
    if not len(lists):
        return []

    shape = get_shape(lists)
    result = create_empty_matrix(shape[1:-1])

    for i in range(shape[0]):
        matrix = lists[i]
        for index in iter_index(shape[1:]):
            element = get_element(matrix, index)
            if i == 0:
                append_element(result, index, element)
            else:
                set_element(result, index, element, operator)
    return result


# %%
if __name__ == "__main__":
    m1 = [
        [
            [
                [1, 2, 'hello']
                for _ in range(3)
            ]
            for _ in range(2)
        ]
        for _ in range(2)
    ]

    m2 = [
        [
            [
                [1, 2, ' world']
                for _ in range(3)
            ]
            for _ in range(2)
        ]
        for _ in range(2)
    ]

    actual = add(m1, m2)
    shape = get_shape(actual)
    print(shape)
    print(actual)

    expected = [
        [
            [
                [2, 4, 'hello world']
                for _ in range(3)
            ]
            for _ in range(2)
        ]
        for _ in range(2)
    ]
    assert actual == expected
    print('Good Job!')
