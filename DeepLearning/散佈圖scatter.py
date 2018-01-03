# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:35:11 2018

@author: Zhong-Xun Yu
"""

import numpy as np
import matplotlib.pyplot as plt

data = {'a' : np.arange(50),
        'b' : np.random.randint(0, 50, 50),
        'd' : np.random.randn(50) }
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
# 第一個參數 X 軸的輸入陣列，第二個參數是 Y軸的輸入陣列
# C參數是設定標記顏色，s 參數設定標記大小
# data 參數是輸入的資料
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()