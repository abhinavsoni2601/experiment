# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:43:47 2019

@author: Gourav
"""

a="hello"
def rev(b):
    d=""
    for x in a[::-1]:
        d=d+x
    print(d)
rev(a)

def rev(a):
    return a[::-1]