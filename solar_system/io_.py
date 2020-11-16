# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:59:30 2020

@author: Nika
"""
A=[]
def take_info():
    global A
    input = open('input.txt', 'r')
    A = input.readlines()
    for i in range(len(A)):
        A[i] = (A[i].split())
    input.close()
    return A
    

def save_info():
    global A
    input = open('input.txt','w')
    input.close()
    for i in range(len(A)):
        input = open('input.txt','a')
        print(*A[i], file=input)
        input.close()
    return A
#print(take_info())
#print(save_info())
