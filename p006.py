#! /usr/bin/env python
# -*- coding: utf-8 -*-

def sumarithmeticsequence(i, n, step=1):
    """等差数列の和を求める関数"""
    return n * (2*i + (n-1)*step) / 2

def sumpowsequence(n):
    """1からnまでのべき乗の和を求める関数"""
    return n*(n+1)*(2*n+1)/6

if __name__ == '__main__':
    print pow(sumarithmeticsequence(1, 10),2) - sumpowsequence(10)
    print pow(sumarithmeticsequence(1, 100),2) - sumpowsequence(100)
    print pow(sum(range(1,101)),2) - sum(map(lambda x: pow(x,2), range(1,101)))
