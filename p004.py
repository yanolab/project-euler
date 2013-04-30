#! /usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations_with_replacement as combinations
from operator import itemgetter

def ispalindromic(num):
    """回文数かどうかを判定する関数"""
    strnum = str(num)
    return strnum == strnum[::-1]

def palindromicnumbers(min, max):
    """min-maxの範囲内数の組み合わせのかけ算で生成される回文数を順に返すジェネレータ"""
    order = 1 if min < max else -1
    return ((x[0] * x[1],) + x for x in combinations(xrange(min, max, order), 2) if ispalindromic(x[0] * x[1]))

if __name__ == '__main__':
    # 先頭が最大の組み合わせとは限らないのでソートして取得する。 <- 速度低下要因
    print sorted(palindromicnumbers(999, 100), key=itemgetter(0), reverse=True)[0]
