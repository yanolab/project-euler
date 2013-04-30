#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
from itertools import imap, ifilter

def isprime(num):
    return all(imap(lambda x: num % x, xrange(2, int(math.sqrt(num)) + 1)))

def primefactors(num):
    factors = ifilter(lambda x: num % x == 0, xrange(int(math.sqrt(num)), 2, -1))
    return (x for x in factors if isprime(x))

if __name__ == '__main__':
    print next(primefactors(600851475143))
