# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:04:48 2017

@author: Zhong-Xun Yu
"""
class Vehicle:
    def __init__(self, name, engine):
        self.__name = name
        self.__engine = engine
        
    def getName(self):
        return self.__name    # 存取私有name的屬性
    
    def getEngine(self):
        return self.__engine   # 存取私有engine屬性
    
    def setEngine(self, engine):   # 設定引擎名稱
        self.__engine = engine   # 呼叫 engine回傳到 self
        
class Car(Vehicle):
    def __init__(self,name,engine,electric):
        super().__init__(name,engine)      # 呼叫父類別的建構函數
        self.__electric = electric     # 私有屬性前要加上 __
        
    def getCarName(self):
        print("名字: " + self.getName())
        print("引擎: " + self.getEngine())
        print("電動車: " + self.__electric)        


    def getAuto(self):
        print("自動駕駛車")
        
# 實體化
myCar = Car("特斯拉", "磁電Engine", "電力")
myCar.getCarName()
myCar.getAuto()
        