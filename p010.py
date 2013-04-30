#! /usr/bin/env python
# -*- coding: utf-8 -*-

import p007

from math import sqrt
from itertools import takewhile as take

if __name__ == '__main__':
    print sum(take(lambda x: x <= 2000000, p007.primes()))
