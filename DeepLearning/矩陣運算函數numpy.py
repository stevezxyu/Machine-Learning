# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:29:48 2018

@author: Zhong-Xun Yu
"""

import matplotlib.pyplot as plt
import numpy as np    # 處理陣列的函式庫
t=np.arange(0.,5.,0.2)
print(t)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()