# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:53:15 2017

@author: Zhong-Xun Yu
"""
class MyClass:
    i = 12345   # class內的成員屬性 i
    
print(MyClass.i)   # 呼叫類別的成員屬性


class Complex:
    # 實體建構
    # __init__(self,..)為建構函數, 實體化物件時會呼叫它
    def __init__(self, realpart, imagpart): 
        # self 為自己這個物件, 屬於類別的成員
        self.r = realpart
        self.i = imagpart

x=Complex(3.0,-4.5)
print(x.r , x.i)    # 呼叫 r 屬性和 i 屬性
