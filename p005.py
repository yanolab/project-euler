#! /usr/bin/env python
# -*- coding: utf-8 -*-

import p003
import operator

def primes(max):
    """2-maxまでの間の素数を返すジェネレータ"""
    return (x for x in xrange(2, max+1) if p003.isprime(x))

def commonprimes(lst=[]):
    """lstに共通の素因数を返すジェネレータ"""
    primenumbers = list(primes(max(lst)))

    while(len(lst) > 0):
        for prime in primenumbers:
            if not all(map(lambda x: x%prime, lst)):
                lst = filter(lambda x: x > 1, map(lambda x: x/prime if x%prime == 0 else x, lst))
                yield prime

def lcm(lst=[]):
    """複数項の最小公倍数を返す関数"""
    return reduce(operator.mul, commonprimes(lst))

if __name__ == '__main__':
    print lcm(xrange(21))
