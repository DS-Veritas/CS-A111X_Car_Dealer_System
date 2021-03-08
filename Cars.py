# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 00:14:39 2019

@author: Jeheon Kim
"""


class Car:
    
    def __init__(self, model_name, model_description, register_id, price):
        self.__name = model_name
        self.__id = register_id
        self.__description = model_description
        self.__price = float(price) 
        
        
    def get_model_name(self): 
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_description(self):
        return self.__description
    
    def get_price(self):
        return self.__price 
    
    def __str__(self):
        return self.__name + ", " + self.__description + ", " + self.__id + ", " + str(self.__price) + " EUR" 