# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:07:46 2021

@author: dennis
"""

a=[]
for i in range(1,11):
    x=int(input("dose arithmo:"))
    while not(x>=0):
       x=int(input("dose arithmo:")) 
    a.append(x)

maximum=a[0]
thesi=0
for i in range(1,10):
    if a[i]>maximum:
        maximum=a[i]
        thesi=i

maximum
thesi
    