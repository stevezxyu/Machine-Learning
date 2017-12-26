# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:49:40 2017

@author: Zhong-Xun Yu
"""

import sys
def displaySalary(salary):
    if salary<0:
        raise ValueError('薪水為正')
    print("薪水: "+str(salary))
    
try:
    Salary=eval(input("請輸入薪水: "))  # eval 計算單一個表達式的值
    displaySalary(Salary)
except OSError as err:
    print("OSError : (0)", format(err))
except ValueError:
    print("請輸入薪水值為正")
except:
    print("Unexcepted error: ", sys.exc_info()[0])