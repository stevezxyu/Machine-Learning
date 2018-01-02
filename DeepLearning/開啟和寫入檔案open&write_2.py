# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:39:56 2018

@author: Zhong-Xun Yu
"""

fp=open('file.txt', 'r')
if fp!=None:
    str=fp.read()
    print(str)
fp.close()
fp=open('file.txt', 'r')
if fp!=None:
    strList=fp.readlines()
    print(strList)
fp.close()