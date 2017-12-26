# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:37:35 2017

@author: Zhong-Xun Yu
"""
import sys
try:
    f=open('mysql.py')
    s=f.readline()   # 讀取一行
    i=int(s.strip())   # strip移除字串開頭
except OSError as err:     # 找不到檔案的 Error
    print("OSError:(0)", format(err))    # format 將資訊列印出來
except ValueError:
    print("Could not convert data to integer.")
except:
    print("Unexcepted error: ", sys.exc_info()[0])