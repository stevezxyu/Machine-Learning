# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:17:48 2017

@author: Zhong-Xun Yu
"""
class Dog:
    kind='small dog'
    def __init__(self, name):
        self.name=name

d=Dog('small dog')
e=Dog('very small dog')

type(d)
type(e)

print(d.name)
print(e.name)
