# Напишите функцию, которая перебирает натуральные числа от 1 до N включительно
# и раскладывает каждое число на простые множители.
# Результат можно выводить на экран либо копить в любой структуре данных.


PRIMES_LIST = []  # list of prime numbers for reuse inside the while loop in prime_factors_brute_force()


def gen_primes(limit=None, limitless=True):
    '''
    Sieve of Eratosthenes prime generator algorithm
    marks off all the multiples of 2, 3, 5, 7 and 11. The rest are all prime numbers.
    if limit=None and limitless=True, 
    :return: yield next prime number each time called
    source: http://code.activestate.com/recipes/117119/, 
    https://stackoverflow.com/questions/25706885/generator-function-for-prime-numbers?rq=1
    >>> list(gen_primes(limit=100, limitless=False))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    '''
    D = {}
    q = 2
    while limitless or q <= limit:
        if q not in D:  # q is prime and not in multiple dictionary
            yield q
            D[q * q] = [q]  # add multiples of 2, 3, 5, 7, 11 to the dictionary
        else:  # q is composite
            for p in D[q]:  # D[q] is the list of primes that divide it
                D.setdefault(p + q, []).append(p)  # we'll mark the next multiples of its witnesses
            del D[q]
        q += 1


def prime_factors_brute_force(n):
    '''
    brute-force algorithm, divides n by prime numbers from 2 to sqrt(n)
    :param n: number to factorize, non-negative integer
    :return: list of prime factors
    source: https://stackoverflow.com/questions/15347174/python-finding-prime-factors
    >>> prime_factors_brute_force(489)
    [3, 163]
    '''
    factors = list()  # factors for return
    i = 0  # PRIMES_LIST elt index
    primes_gen = gen_primes()  # create generator object
    factor = 2  # first factor for conditional
    if n == 0: # in case we get zero as input (not in the conditions
        return [float('inf')]
    while True:
        if n % factor:
            try:
                factor = PRIMES_LIST[i + 1]  # pick next prime number from PRIMES_LIST
                i += 1
            except IndexError:  # if list is exhausted
                PRIMES_LIST.append(next(primes_gen))  # generate next prime number]
        else:
            n //= factor  # move to next n
            factors.append(factor)  # add factor to the fartors list
        if factor ** 2 > n:  # we exhaust all factors 2..sqrt(n)
            primes_gen.close() # stop generator
            break
    if n > 1:
        factors.append(n)  # add residual n to the factors list
    return factors


def create_primes(number):
    '''
    :return: dictionary {number:[*prime_factors]}
    '''
    # enable this if you want print factors on the screen
    # for i in range(number):
    #   print('Prime factorization for {} is {}'.format(i, prime_factors_brute_force(i)))
    D = {}
    for i in range(1, number):
        D.update({i: prime_factors_brute_force(i)})  # statements aren't used inside list comprehensions
    return D


### Unittest part ###

import unittest
from functools import reduce


class TestFile(unittest.TestCase):
    def test_are_prime_factors(self, n=100):
        '''
        test if dict values are prime factors for the key
        '''

        def is_prime(self, n):
            '''
            test if given integer is prime
            :param n: integer
            :return: True if n is prime number
            '''
            for i in range(3, n):
                if n % i == 0:
                    return False
            return True

        for k, v in create_primes(n).items(): # iterate over factors dictionary
            if k == 1:
                self.assertEqual(v, []) # check there is no prime factors for 1
            else:
                self.assertTrue(all(is_prime(self, n) for n in v)) # check if all factors are prime numbers
                self.assertEqual(reduce(lambda x, y: x * y, v), k) # check if factors multiplied are equal to their key

### Run part ###

if __name__ == '__main__':
    print(create_primes(100))

    from matplotlib import pyplot
    import plots


    plots.plotTC(create_primes, 10, 100, 1, 10) # func_name, nMin, nMax, nInc, nTests
    pyplot.show()

    unittest.main()

    # enable this to mean calculation time for the given number argument inside create_primes()
    # print(timeit.timeit("create_primes(100)", setup = 'from __main__ import create_primes', number = 100))
