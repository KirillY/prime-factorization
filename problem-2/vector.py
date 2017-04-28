# Имеется вектор размера N. Необходимо разделить его на M < N равных частей
# (то есть чтобы количество элементов в каждой части было одинаковым).
# Части не должны пересекаться и должны покрывать весь вектор
# (исключение - допускаются промежутки от начала вектора до начала первой части и от конда последней части до конца вектора,
# но в этом случае необходимо добиться, чтобы разница в величине этих промежутков была минимальной).

# Результатом должны являться индексы начала и конца каждой части (либо вывод на экран, либо сохранение в любую структуру данных).

import numpy as np

def divide_vector_into_equal_chunks(vector, M, axis=1):
    '''    
    Split an array (vector) into multiple sub-arrays.
    Allows M to be an integer that does not equally divide the axis.
    :param vector: numpy array
    :param M: integer or 1D array
    :param axis: The axis along which to split, default is 1
    :return: A list of sub-arrays
    source: https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_split.html#numpy.array_split
    >>> x = np.arange(8.0)
    >>> np.array_split(x, 3)
    [array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.])]
    '''
    return np.array_split(vector, M, axis=axis)


if __name__ == '__main__':

    import random

    a = np.random.randint(0, 10, [4, 4])
    print("Initial array: \n{}\nDivided array: \n{}".format(a, divide_vector_into_equal_chunks(a, 2)))
