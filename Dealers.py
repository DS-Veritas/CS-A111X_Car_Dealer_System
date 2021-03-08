# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 00:15:11 2019

@author: Jeheon Kim
"""

from Cars import Car

class Dealer:
    
    # Initial balance for the car dealer is 50,000EUR as cash
    def __init__(self, name, initial_balance = 50000.00):
        self.__name = name
        self.__balance = float(initial_balance)
        # Use append to add car class to inventory
        # When adding a car to the inventory, add purchase price 
        self.__inventory = []
        
    # BUY <register id> "<model description>" <price> : 
    # Buys a car with given register number and model desription at a given price, and adds it to the dealer invetory. 
    # Cash will be decremented accordingly. Note that model description is surrounded by quotes, because it can contain spaces. 
    # Register ID is similar to those used in Finland (e.g. "ABC-123") (+1)    
    def buy(self, model_name, model_description, register_id, price, carList, index):
        if (self.__balance >= price):
            # Adds a car to the dealer's inventory, if the balance is enough to purchase a car
            self.__inventory.append(Car(model_name, model_description, register_id, price))
            del carList[index]
            # Balance will be decremented accordingly
            self.__balance -= price
        else:
            input("Unfortunatley, you don't have enough money to purchase this car.\n" +
                  "Press enter to go back to the list of available cars.") 
    
    # Sells all cars in the auctionList. Remove the cars from the dealer's inventory. And increase the dealer's balance by the highest offer.         
    def sell(self, auctionList):
        for car in auctionList:
            highestBid = sorted(auctionList.get(car), key = lambda x: x[1], reverse = True)[0]
            print("The car, {}\nis sold to the highest bidder, {}, for {}EUR. ".format(car.get_model_name(), highestBid[0], highestBid[1]))
            if highestBid[1] - car.get_price() > 0:
                print("You made a profit of {}EUR from this car.\n".format(highestBid[1] - car.get_price()))
            elif highestBid[1] - car.get_price() < 0:
                print("You made a loss of {}EUR from this car.\n".format(abs(highestBid[1] - car.get_price())))
            else: 
                print("You sold a car for your purchased price. At least, you didn't make a loss...\n")
            self.__inventory.remove(car)
            self.__balance += highestBid[1]
    
    # Printing sales info is implemented in the def sell above, instead.
    # def history will print the total profit and the list of unsold cars, if any.        
    def history(self):
        input("Press enter to see the total profit and the list of unsold cars in your inventory.\n")
        print("Your total profit at this moment: {}EUR\n".format(self.__balance - 50000.00))
        
                
        if (len(self.__inventory) > 1):
            input("However....\n")
            for car in self.__inventory:
                print("- {}".format(car))
            print("\nDon't worry. You still have these {} cars left to sell. Keep going!\n".format(len(self.__inventory)))
        elif (len(self.__inventory) == 1):
            input("However....")
            for car in self.__inventory:
                print("- {}".format(car))
            print("\nDon't worry. You still one car left to sell. Keep going!\n".format(len(self.__inventory)))
        else:
            print("And there is no remaining cars in your inventory...\n" +
                  "Therefore, this is your final profit...\n")
            
        print("Closing the simulation... Good Bye...")
        
    
    def get_inventory(self):
        return self.__inventory
    
    def get_balance(self):
        return self.__balance
    
    def get_money_spent(self):
        return (50000.00 - self.__balance)
        
    # INV : Prints the current inventory along with the following details: 
    #       register number, model description, purchase price. Finally, the current cash balance should be printed. (+1)
    def inv(self):
        # Inventory of cars of the Dealer
        if(len(self.__inventory) > 0):
            counter = 1
            for car in self.__inventory:
                # Here the last car[1] should print the purchase price of the car
                # When a dealer purchases a car, it is added to the dealer's inventory as a tuple (or dictionary) with the purchase price
                print("{}. {}, {}, {} - Purchased price: {}EUR".format(counter, car.get_model_name(), car.get_id(), car.get_description(), car.get_price()))
                counter += 1
            print("\nThe remaining balance is: {}EUR".format(self.__balance))
        else:
            print("\nThere is no car in your inventory. Purchase one from the market first.")
        