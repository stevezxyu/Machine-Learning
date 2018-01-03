# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:49:09 2018

@author: Zhong-Xun Yu
"""

import pandas as pd   # 處理 dataFrame

SalarysDic ={"John" : '50000',
        "Mary" : '20000',
        "Ivy" : '90000',
        "Steve" : '35000',
        "David" : '85000'
        }
myDic = pd.Series(SalarysDic, index=SalarysDic.keys())
print(myDic[0])
print(myDic['Ivy'])
print(myDic[[0,1,3]])
print(myDic[['John', 'Ivy', 'David']])