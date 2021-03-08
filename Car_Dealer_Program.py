# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:29:15 2019

@author: Jeheon Kim
"""

from Cars import Car
from Dealers import Dealer
from Buyers import Buyer

# Check whether input is Int or not - Selection number
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
# Check whether input is Float or not - Offer Amount
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def printCarList(carList):
    counter = 1
    for car in carList:
        print("{}. {}".format(counter, car)) 
        counter += 1
        
    print("\nTotal {} cars are available at this moment".format(len(carList)))
        

def main():
    # CarList.txt contains total of 18 used cars for dealer to purchase within his budget of 50,000EUR
    filename = input("Enter the name of a file ('CarList.txt' for this project): \n")
    try:
        file = open(filename, "r")
        linelist = file.readlines()
        del linelist[0]
        file.close()
        
        carList = []
        for line in linelist:
            line = line.rstrip()
            split = line.split(", ")
            carList.append(Car(split[0],split[1],split[2],split[3]))
            
        dealerName = input("You are a car dealer. Please type your name: \n")
        dealer = Dealer(dealerName)
        print("\nHello {}. You are a car dealer and have a budget of 50,000EUR.\n".format(dealerName) + 
              "First, you can purchase cars to sell from the market within your budget.\n")
        print("There are three options you can select as a dealer.")
        
        choice = 0 
        while (choice != "3"):
            choice = input("[1] Check available cars in the market and make a purchase.\n" +
                           "[2] Check your inventory of purchased cars.\n" +
                           "[3] Quit (Only when you finished purchasing cars)\n" + 
                           "\nChoose the number and press enter: "
                           )
            if choice == "1":
                nextChoice = ""
                # QUIT : exit program. "Quit" and "quit" both are accepted
                while nextChoice != "Quit" or nextChoice != "quit":
                    print("Available cars in the market at this moment:\n")
                    printCarList(carList)
                    nextChoice = input("If you want to purchase a car, choose the number and press enter...\n" + 
                                       "or to go back to the list of options, please type '{}' and press enter: ".format("Quit"))
                    if nextChoice.lower() == "quit":
                        print("Going back to the list of options...")
                        break
                    elif isInt(nextChoice) and int(nextChoice) in range(1, len(carList) + 1):
                        index = int(nextChoice) - 1 
                        # BUY <register id> "<model description>" <price> : Buys a car with given register number and model desription at a given price, and adds it to the dealer invetory.
                        dealer.buy(carList[index].get_model_name(), carList[index].get_description(), carList[index].get_id(), carList[index]. get_price(), carList, index)
                        
                    else:
                        input("Wrong input. Please choose a index number of available car or 'Quit' to go back.\n")
                
            elif choice == "2":
                dealer.inv()
                input("Press enter to go back to the list of options.")
                
            elif choice == "3":
                input("Now dealer's part is over. Press enter to move on to the buyer's part.")
            else:
                print("\nYou typed invalid number. Please choose a number between 1 to 3.")
                input("Press enter to go back to the list of options.")
                
        # Continue with the Buyer's part - Implement OFFER / SELL / HISTORY / QUIT
        
        buyerList = []
        print("There are five buyers in this simulation, please type their names.")
        countText = ["first","second","third","fourth","last"]
        textCounter = 0 
        for counter in range (1, 6):
            name = input("Please type your {} buyer name for the bidding process:\n".format(countText[textCounter]))
            buyerList.append(Buyer(name))
            textCounter += 1
        
        input("Buyers' names are registered successfully. Press enter to continue.")
        
        auctionList = {}
        for buyer in buyerList:
            print("\nHello {}. Now, it's your turn.\nYou can make an offer to a car from the dealer's inventory.".format(buyer.get_name()))
            #input("Press enter to continue...")
            print("\nHere are a list of available cars in the dealer's inventory at this moment:\n")
            innerCounter = 1
            for car in dealer.get_inventory():
                print("{}. {}, {}, {}".format(innerCounter, car.get_model_name(), car.get_description(), car.get_id()))
                innerCounter += 1
            counter += 1
            
            # Data sturcture (dictionary) where the bidding history will be saved
            
            
            number = ""
            while (not (isInt(number) and int(number) in range(1, len(dealer.get_inventory()) + 1))):
                number = input("Please select the number of the car you would like to bid for: ")
                
                if (not (isInt(number) and int(number) in range(1, len(dealer.get_inventory()) + 1))):
                    print("Please type the number of the car in the list...")
            
            if isInt(number) and int(number) in range(1, len(dealer.get_inventory()) + 1):
                amount = "Test"
                while not isFloat(amount) or  float(amount) <= 0:
                    amount = input("Please type the amount you want to offer to this car: ")
                    if (not isFloat(amount) or float(amount) <= 0):
                        print("Wrong input. Please type the valid offer amount: positive integer or decimal number > 0")
                    else:
                        # Calls buyer's OFFER method to make an offer to a chosen car
                        buyer.offer(buyer.get_name(), dealer.get_inventory()[int(number) - 1], amount, auctionList)
            
            else: 
                input("Please type the number of the car in the list.")
            
        input("Now back to the dealer's part again. Press enter to continue.")
        
        # Implement sell (in the bidding list), history
        
        choice = 0 
        while (choice != "3"):
            choice = input("[1] Check a bid list.\n" +
                           "[2] Check your current inventory.\n" +
                           "[3] Quit (This will end the simulation and returns your total profit)\n" + 
                           "\nChoose the number and press enter: "
                           )
            
            if choice == "1":
                for biddedCar in auctionList:
                    print("\n{}, {}, {}\nPurchased price: {}".format(biddedCar.get_model_name(), biddedCar.get_description(), biddedCar.get_id(), biddedCar.get_price()))
                    print("-> This car has recevied total {} offer(s).\n".format(len(auctionList.get(biddedCar))))
                    
                    innerCounter = 1
                    # print the list of cars with bid history in decreasing offer amount order
                    for bidInfo in sorted(auctionList.get(biddedCar), key = lambda x: x[1], reverse = True):
                        print("Bid {}. An offer of {}EUR received from the {}.".format(innerCounter, bidInfo[1], bidInfo[0]))
                        innerCounter += 1
                        
                input("Press enter to go back to the previous step...")
                        
                        
            elif choice == "2":
                dealer.inv()
                print("\nTotal spent on purchasing cars is: {}EUR".format(dealer.get_money_spent()))
                input("Press enter to go back to the list of options.")
                
            # Auction cannot choose whether to sell or not based on the given bids
            # If there is a bid, you must sell and if there are more than 1 bid, sell to the highest bidder
            # Therefore, here the seller doesn't get to choose which car to sell but is forced to sell
            # all cars that have recived offer from the bidders. 
            # So, when choose "quit" -> all cars in auctionList will be sold to the highest bidder
            elif choice == "3":
                input("Processing sales to the highest bidders...\n" +
                      "Press enter to see your profit for each car sold.\n")
                dealer.sell(auctionList)
                dealer.history()
                
            else:
                print("\nYou chose invalid number. Please choose a number between 1 to 3.")
                input("Press enter to go back to the list of options.")
        
        
        
        
        
                
            
    except OSError:
        print("Error in reading file ", filename, ". closing program...")
 

main()