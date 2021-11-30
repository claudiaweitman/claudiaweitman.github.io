# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def standev (datalist):
    
    N = 0
    for i in datalist:
        N+=1
    
    #Add
    Mean = sum(datalist)/N
    
    variance = list(map(lambda x: x - Mean, datalist))
    varsquare = list(map(lambda x: x*x, variance))
    n=N-1
    a=sum(varsquare)/(n)
    b=a**0.5
    return N, Mean, b
