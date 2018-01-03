# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:09:33 2018

@author: Zhong-Xun Yu
"""

import matplotlib.pyplot as plt

month1 = [1,2,3,4,5,6,10,12]
month2 = [1,3,4,5,6,7,11,12]
sales1 = [20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000]
sales2 = [10000, 20000, 30000, 15000, 120000, 80000, 60000, 210000]
plt.plot(month1, sales1, lw=2, label='Ivy Lin')
plt.plot(month2, sales2, lw=2, label='Steve Yu')
plt.xlabel('month')
plt.ylabel('dollars')
plt.legend()    # 畫標籤 label
plt.title('matplotlib example')
plt.show()