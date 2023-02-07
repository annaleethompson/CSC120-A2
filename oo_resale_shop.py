from computer import *

computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)

class ResaleShop:

    # What attributes will it need?
    inventory = []
    itemID: int = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID


    # What methods will you need?
    def buy(self, itemID):
        #Call computer constructor
        
        # Add it to the resale store's inventory
    
        #Call inventory.append() to add new computer
        self.inventory.append(computer)
       
        self.inventory[itemID] = computer
        itemID += 1 # increment itemID
        computer_id = itemID
        print("Done.\n")
    

    def print_inventory(self, item_id):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
    
        
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")


        