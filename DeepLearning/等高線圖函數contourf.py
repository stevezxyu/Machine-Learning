# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:54:09 2018

@author: Zhong-Xun Yu
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)