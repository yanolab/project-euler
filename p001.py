#! -*- coding: utf-8 -*-

import time
from itertools import chain

def oldstyle1(bellow):
    sum = 0
    for x in xrange(1, bellow):
        if x % 3 == 0 or x % 5 == 0:
            sum += x

    return sum

def oldstyle2(bellow):
    sum = 0

    m = 0 if bellow % 3 == 0 else 1
    for x in xrange(1, bellow/3+m):
        sum += x*3

    m = 0 if bellow % 5 == 0 else 1
    for x in xrange(1, bellow/5+m):
        sum += x*5


    m = 0 if bellow % 15 == 0 else 1
    for x in xrange(1, bellow/15+m):
        sum -= x*15

    return sum

def functionalstyle(bellow):
    def _multiples(num):
        return (x * num for x in xrange(1, (bellow / num) + (bellow % num and 1)))

    return sum(_multiples(3)) + sum(_multiples(5)) - sum(_multiples(15))

def mathstyle(bellow):
    def _multiples(num):
        m = (bellow-1) / num
        return (m * (m + 1)) / 2 * num

    return _multiples(3) + _multiples(5) - _multiples(15)


if __name__ == '__main__':
    s = time.time()
    print oldstyle1(1000000), time.time() - s

    s = time.time()
    print oldstyle2(1000000), time.time() - s

    s = time.time()
    print functionalstyle(1000000), time.time() - s

    s = time.time()
    print mathstyle(1000000), time.time() - s
