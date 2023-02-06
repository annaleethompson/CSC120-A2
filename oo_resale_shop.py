from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []
    itemID = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self, inventory):
        #Call computer constructor
        computer = computer.create_computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)

        # Add it to the resale store's inventory
        print("Buying", computer["description"])
        print("Adding to inventory...")
    
        #Call inventory.append() to add new computer
        inventory.append(computer)
        itemID += 1 # increment itemID
        inventory[itemID] = computer
        computer_id = itemID
        print("Done.\n")
    
    def sell(self):
        pass
        

def main():
     print("-" * 21)
     print("COMPUTER RESALE STORE")
     print("-" * 21)

     # Add it to the resale store's inventory
     

        