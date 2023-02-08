from computer import *
from typing import Dict

egg_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
class ResaleShop:

    # What attributes will it need?
    inventory: Dict = {}  
    itemID: int = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, name):
        self.inventory = inventory
        self.name = name


    # What methods will you need?
    def buy(self, computer):
        self.itemID +=1
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "bought!")
        return self.itemID
        #Call computer constructor
        #computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
     
        # Add it to the resale store's inventory
    
        #Call inventory.append() to add new computer
        

    def print_inventory(self):
        # If the inventory is not empty
        if len(self.inventory)>=1:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else: 
            print("No items in Inventory")
    
        
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def refurbish2(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            Computer.refurbish(computer)
            # if int(self.year_made) < 2000:
            #     self.price = 0 # too old to sell, donation only
            # elif int(computer["year_made"]) < 2012:
            #     self.price = 250 # heavily-discounted price on machines 10+ years old
            # elif int(self.year_made) < 2018:
            #     self.price = 550 # discounted price on machines 4-to-10 year old machines
            # else:
            #     self.price = 1000 # recent stuff

            # if new_os is not None:
            #     computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    def update_price(self, computer, new_price):
        computer = self.inventory[self.itemID]
        computer.price = new_price
        #Computer.update_price(itemID, new_price)

#Tests
Egg_shop = ResaleShop({}, "Egg's Shop")

Egg_shop.buy(egg_computer)
Egg_shop.print_inventory()
#Egg_shop.sell(1)
#Egg_shop.print_inventory()
Computer.print_product_details(egg_computer)
Egg_shop.refurbish2(1)
Computer.print_product_details(egg_computer)
Egg_shop.update_price(egg_computer, 600)
Computer.print_product_details(egg_computer)