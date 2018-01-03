# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:45:33 2018

@author: Zhong-Xun Yu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4]);
y = np.array([5,6,7]);
# xx, yy是 meshgrid()回傳陣列
xx, yy = np.meshgrid(x, y)   # meshgrid 畫網狀圖
print(xx)
print(yy)
plt.plot(xx, yy, marker='.', color='k', linestyle='none')
plt.show()