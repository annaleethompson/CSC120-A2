''' Filename: oo_resale_shop.py
    Decription: Object oriented code that contains the resale shop class and functions to buy, print inventory, sell, refurbish, and update price. 
    A part of CSC 120-02: Object-Oriented Programming, Smith College Spring 2023, A2: Object-ification
    Author: Anna-Lee Thompson (@annaleethompson)
    Date: February 8, 2023
'''
#Imports the computer class and its functions
from computer import *
#Imports Dict from typing module
from typing import Dict

#Example computer
egg_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)

#Creates computer class that has attributes including inventory, itemID, and name. 
class ResaleShop:

    # Attributes we need:
    inventory: Dict = {}  
    itemID: int = 0

    # ResaleShop constructor assigning attributes
    def __init__(self, inventory, name):
        self.inventory = inventory
        self.name = name

    # Function "buys" computer by adding it to the resale shop inventory
    def buy(self, computer):
        self.itemID +=1
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "bought!")
        return self.itemID
        
    #Function prints the item ID of the item or sends a message if there are no items in the inventory
    def print_inventory(self):
        # If the inventory is not empty
        if len(self.inventory)>=1:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else: 
            print("No items in Inventory")
    
    #Function "sells" computer by removing the item ID from the inventory or sends a message if that item isn't in the inventory.    
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    #Function locates the computer and then calls on the refurbish function in the computer module to change the price or operating system. Returns a message if item isn't found. 
    def refurbish2(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            Computer.refurbish(computer, new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    #Function updates the price of the computer with the new (inputed) price
    def update_price(self, computer, new_price):
        computer = self.inventory[self.itemID]
        computer.price = new_price

#Tests for each function
Egg_shop = ResaleShop({}, "Egg's Shop")
Egg_shop.buy(egg_computer)
Egg_shop.print_inventory()
#Egg_shop.sell(1)
#Egg_shop.print_inventory()
Computer.print_product_details(egg_computer)
Egg_shop.refurbish2(1, "Windows")
Computer.print_product_details(egg_computer)
Egg_shop.update_price(egg_computer, 600)
Computer.print_product_details(egg_computer)