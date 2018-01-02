# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:47:10 2018

@author: Zhong-Xun Yu
"""
fp=open('file.txt', 'w')
if fp !=None:
        print("檔案開啟成功")
fp.close()
fp=open('file.txt', 'w')
if fp!=None:
    fp.write('小白')
fp.close()
fp=open('file.txt', 'r')
if fp!=None:
    str=fp.read()   # 字串被讀取出來
    print(str)
fp.close()

fp=open('file.txt', 'r')
if fp!=None:
    fp.write('小新')
fp.close()
