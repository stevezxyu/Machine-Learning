# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:34:26 2017

@author: Zhong-Xun Yu
"""
while True:
    try:
        x=int(input("請輸入一個數字: "))
        break
    except ValueError:
        print("input error")