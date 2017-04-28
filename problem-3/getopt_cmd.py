# Напишите простую реализацию функции для разбора параметров командной строки (getopt).

# Полагаем, что нам требуется структура данных,
# содержащая заранее известный допустимый набор параметров различного типа - строки,
# целые, числа с плавающей точкой и т. д., а также признак, является ли этот параметр обязательным.
# Полагаем, что параметры могут передаваться только в "длинном" формате с обязательным "--" перед именем параметра
# (то есть "--my-option-name my-option-val", "--my-option-name=my-option-val", "--my-boolean-option").
# Параметров может быть несколько.
# Функция должна обязательно уметь обрабатывать параметр "--help" (если он указан в списке параметров при вызове функции),
# выводящий пример использования (необязательные параметры должны выводиться в квадратных скобках).
#
# Реализация требуется на С++ и/или Python.

import sys
import getopt
from contextlib import contextmanager


@contextmanager
def error_handler():
    '''
    exception handler for main()
    '''
    try:
        yield
    except ValueError:
        print('ERROR: Invalid arguments')


def usage():
    s = '''Usage: [option]... [number]...
    Support only long options
    --sum       sum of numbers
    --max       max of numbers
    --help      usage
    '''
    print(s)


def maximum(lst):
    '''
    convert list elements to numbers and return max elt
    prints result
    :return: None
    >>> maximum([52, 35])
    Maximum of given numbers is: 52
    '''
    m = max([int(n) for n in lst])
    print('Maximum of given numbers is: {}'.format(m))


def summ(lst):
    '''
    convert list elements to numbers and return their sum 
    prints result
    :return: None
    >>> summ([25, 62])
    Sum of given numbers is: 87
    '''
    s = sum([int(n) for n in lst])
    print('Sum of given numbers is: {}'.format(s))


def main():
    '''
    cmd line utilite, calculate sum and/or max for given int or float numbers
    :return: None
    '''
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['sum', 'max', 'help'])  # parse arguments
    except getopt.GetoptError as err:  # print help information and exit
        print('Option "{}" is not recognized'.format(err.opt))
        usage()
        sys.exit(2)
    for opt, arg in opts:  # we do not use option argument values in this implementation
        if opt in '--help':
            usage()
        elif opt in '--max':
            with error_handler():
                maximum(args) # trailing args
        elif opt in '--sum':
            with error_handler():
                summ(args)
        else:
            usage()
            sys.exit(2)


if __name__ == "__main__":
    main()
