# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:44:48 2018

@author: Zhong-Xun Yu
"""

import numpy as np
from scipy import linalg as la  # 做線性代數運算
A = np.array([[1,3,5], [2,5,1], [2,3,8]])
# 做反矩陣運算
print("做反矩陣運算")
print(A)
print(la.inv(A))
print(A.dot(la.inv(A)))
print("---------------")

# 行列式的值運算
B = np.array([[1,2], [3,4]])
print("行列式的值運算")
print(B)
print(la.det(B))
print("---------------")

C = np.array([[1,5,2], [2,4,1], [3,6,2]])
lna,v= la.eig(A)
l1,l2,l3 = lna
# 求出 eigenvalue 
print("求出 eigenvalue ")
print(l1,l2,l3)
print("---------------")
# 求出 eigenvector
print("求出 eigenvector")
print(v)
print("---------------")
print(v[:,0])
print(v[:,1])
print(v[:,2])
v1 = np.array(v[:,0]).T   # 轉置矩陣
print("---------------")
print("轉置矩陣")
print(v1)
print(la.norm(A.dot(v1)-l1*v1))