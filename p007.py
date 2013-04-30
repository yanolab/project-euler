#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
from bisect import bisect
from itertools import count, dropwhile as drop, imap as map, izip as zip, islice as slice

def primes():
    """素数を2から順に返すジェネレータ"""
    yield 2
    _primes = [2]
    for i in count(3):
      if all(map(lambda x: i%x, slice(_primes, 0, bisect(_primes, math.sqrt(i))))):
          _primes.append(i)
          yield i

if __name__ == '__main__':
    print next(drop(lambda x: x[0] <= 10000, zip(count(1), primes())))
