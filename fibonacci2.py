# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:51:46 2018

@author: sakai kotaro
"""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

print(fib(2018))  