#! /usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import ifilter, takewhile, count
from functools import partial
from operator import add

def fibo(first=0, second=1):
  for _ in count(0):
    n = first + second
    yield n
    first, second = second, n

if __name__ == '__main__':
    even = partial(ifilter, lambda x: x % 2 == 0)
    under4M = partial(takewhile, lambda x: x < 4000000)

    print reduce(add, even(under4M(fibo())))
