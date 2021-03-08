# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:38:18 2019

@author: Jeheon Kim
"""

from Cars import Car

class Buyer:
    
    def __init__(self, name):
        self.__bid_list = []
        self.__name = name
        
    # Buyer can make an offer to a single car they like the most
    # Buyer's name and offered amount will be saved in the auctionList dictionary    
    def offer(self, bidder_name, car_info, bid_amount, auctionList):
        if auctionList.get(car_info) is None:
            auctionList[car_info] = [[bidder_name, float(bid_amount)]]
        else:
            auctionList.get(car_info).append([bidder_name, float(bid_amount)])
        
        # Also, adds a bidded car to the buyer's bid_list
        self.__bid_list.append(car_info)
    
    def get_name(self):
        return self.__name
    
    def get_bid_list(self):
        return self.__bid_list
    
    # Won't be used in the simulation but buyer prints its bidded car
    def __str__(self):
        for car in self.__bid_list:
            print("You have bid for {}.".format(car.get_model_name()))
    
        