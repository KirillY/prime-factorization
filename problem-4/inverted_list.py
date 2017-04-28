# Имеется простой односвязный список размера N.
# Необходимо реализовать алгоритм, который перепаковывает список так,
# чтобы за первым элеметом следовал последний, затем второй, затем предпоследний и т. д. Пример работы алгоритма:
# исходный список: 1-2-3-4-5-6-7-8
# перепакованный список: 1-8-2-7-3-6-4-5.
# Оценить сложность предложенного алгоритма.


# enable this for the plot
# def take_first_last(N):
#     result = list() # O(1)
#     lst = [252]*N # O(N)
#     for i in range((len(lst)+1) // 2): # O(N)
#         result.append(lst[i]) # O(1)
#         result.append(lst[-i - 1]) # O(1)
#     return result[:-1] if length%2 else result # O(1)

def take_first_last(lst):
    '''
    algorithm complexity is O(N)
    :param lst: list
    :return: recombined list 1-2-3-4-5-6-7-8 -> 1-8-2-7-3-6-4-5
    >>> take_first_last([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 8, 2, 7, 3, 6, 4, 5]
    >>> take_first_last([])
    []
    >>> take_first_last([1, 2, 3, 4, 5, 6, 7])
    [1, 7, 2, 6, 3, 5, 4]
    '''
    result = list()  # O(1)
    length = len(lst) # O(1)
    for i in range((length+1) // 2):  # O(N); +1 to capture the middle element when we have odd number of elts
        result.append(lst[i])  # O(1)
        result.append(lst[-i - 1])  # O(1)
    return result[:-1] if length%2 else result # O(1); cut the excess middle elt if lst has odd length


if __name__ == '__main__':
    from matplotlib import pyplot
    import plots

    # comment next line for the plot
    print(take_first_last([1, 23, 4, 6, 7, 8]))

    # enable this for the plot
    # plots.plotTC(take_first_last, 10, 1000, 10, 100)
    # pyplot.show()
