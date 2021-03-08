This is an instruction for the final project: Car Dealer. 


*********************************************************************************************************************************************************

# Since the demostrantion is cancelled, the program is modified to be easy for TAs to follow. 
   There is no need for TA's to input "Car Model Name" or "Registered Number" or etc to puchase a car from the market. 
   Available cars will be shown as a list with each index number, and all need to do is choose the number of the car. 

   However, code mechanism behind works the same as requirement. 
   For example, when the dealer choose the number of the car wish to purchase..

   it will run the following method defined in the dealer's class

   "dealer.buy(carList[index].get_model_name(), carList[index].get_description(), carList[index].get_id(), carList[index]. get_price(), carList, index)"

   which is defined as following:

   "def buy(self, model_name, model_description, register_id, price, carList, index):"

   For the buyer's part (purchase car from the dealer), it is required to input offer amount. 

*********************************************************************************************************************************************************

Requirements: 

1. BUY <register id> "<model description>" <price> 
: Buys a car with given register number and model desription at a given price, and adds it to the dealer invetory. 
Cash will be decremented accordingly. Note that model description is surrounded by quotes, because it can contain spaces. 
Register ID is similar to those used in Finland (e.g. "ABC-123") (+1)

... is implemented in the Dealer.py

2. INV 
: Prints the current inventory along with the following details: 
register number, model description, purchase price. Finally, the current cash balance should be printed. (+1)

... is implemented in the Dealer.py

3. OFFER <name> <register id> <offer> 
: Register an offer for a car with given register number. 
This is not yet a sale, but the offer is stored in the system, waiting for other offers. (+1)

... is implemented in the Buyers.py

4. SELL <register id> : 
Sell the given car to the highest offer made for that car. Increase balance accordingly, and remove car from inventory. 
All offers for the car will be removed from the offers list. (+1)

... is implemented in the Dealers.py

5. HISTORY 
: Prints the sales history of cars sold. It should print the following details: 
register number, model description, purchase price, sell price, buyer name for each car sold. 
Finally, the total profit (or loss) should be printed. (+1)

... is implemented in the Dealers.py
Part of the function (prints the sales history) is implemented in the def SELL instead. 
def HISTORY will print the total profit and the list of unsold cars left in the inventory (If any) 


*********************************************************************************************************************************************************

Please run the "Car_Dealer_Program.py" for the simulation.
The program is divided into 3 parts: Dealer, Buyers and again Dealer. 

In the first part, as a dealer, you can purchase used cars in the market within your 50,000EUR budget. 
Initially (in the CarList.txt file), there are 18 cars available and you can purchase one by typing the index number of the car. 
You will be able to check whether the purchase was made or not by checking the number of available cars in the market. 
- If purchase was successfully made, the number of available car should be decreased by 1. 
- If purchase was not successfully made because of not enough budgetm, it will return this error message: 
  "Unfortunatley, you don't have enough money to purchase this car. Press enter to go back to the list of avialable cars." 
- If purchase was not successfully made because of unsupported input (Only integer is allowed), it will return following message: 
  "If you want to purchase a car, choose the number and press enter" 

You can check the list of purchased cars from the [2] Check your current inventory.
The cars in your inventory will appear with its information and purchased price, then lastly, your remaining balance. 

When you select "[3] Quit (Only when you finished purchasing cars)" 

The second part will start as buyers. Initially, there are 5 buyers for this project. 
(You can simply name them as, buyer1 / buyer2/ buyer3 / buyer4 / buyer5) 
***For the better visibility of the text, I highly recommend to enlarge the console.***

On each turn, a buyer can make an offer to a single car. (Type the index number of a car, and offer amount [float]).
In case of wrong input (not float), following message will be returned "Wrong input. Please type the valid offer amount: positive integer or decimal number > 0"
***To test whether the car is sold to the highest bid or not, please try multiple buyers to bid on same car.***

Once all 5 buyers made an offer, it continues to the last part as a dealer again. 

Dealer can check the list of bids on his cars in inventory. (Since 5 buyers can make an offer to a single car, the max number of bidded cars is 5) 
The bid list will show the information of car, your purchased price (from the market), bidder's name and the offer amount

Since this is an auction, the dealer has no choice but to sell cars to the highest bidder. 
When select "quit", the final summary will show up: 
- the sales information (buyer's name, price and the profit you made from this sale)
- if you made a profit, following message will be returned: "You made a profit of ~ EUR from this car"
- if you made a loss, following message will be returned: "You made a loss of ~ EUR from this car" 
- if you sold a car at a price you purchased, "You sold a car for your purchased price. At least, you didn't make a loss..." will be returned.

And lastly, (when you press enter to continue) your total profit will be printed, and your leftover cars in the inventory (that are not sold) will be printed. 
- if there is / are unsold car(s) left in your inventory, "However," + list of cars + "Don't worry. You still have these ~ cars left to sell. Keep going!" will be printed.
- if there is no car left in your inventory, "And there is no remaining cars in your inventory.", "Therefore, this is your final profit..." will be printed. 

It would be difficult to see a positive profit unless you sell all cars you purchased. To see the positive profit, purchase 5 cars (as a dealer) and sell all to each buyer. 

Required functions mentioned in the final project instructions are commented with detailed information (How it is implemented and etc) 

Thanks for reading this long text so far. 

*********************************************************************************************************************************************************

* It is desinged that the dealer will purchase at least 1 car and each buyer will make an offer to a car. 
  Therefore, the possible error, from the situation where dealer buys none, buyers make no offer, is not handled. 
* Only the unexpected input by a user is handled. (As requied in the instruction) 