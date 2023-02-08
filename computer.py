''' Filename: computer.py
    Decription: Object oriented code that contains the computer constructor and functions to update price, refurbish, check price, and update details
    A part of CSC 120-02: Object-Oriented Programming, Smith College Spring 2023, A2: Object-ification
    Author: Anna-Lee Thompson (@annaleethompson)
    Date: February 8, 2023
'''
#import Optional container from typing module
from typing import Optional

#Creates computer class that has attributes including decription, processor type, hard drive capacity, memory, opertating system, year made, price. 
class Computer:

    # Attributes we need:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Computer constructor assigning attributes
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    #Function that updates the computer (self) price by assigning it to the new (inputed) price
    def update_price(self, new_price):
            self.price = new_price

    #Fucntion that changes the price and/or changes opperating system based on the year the computer was made. If a new operating system is inputed the computer will be assigned the new opperating system. 
    def refurbish(self, new_os: Optional[str] = None):
            if self.year_made < 2000:
                self.price = 0 # too old to sell, donation only
            elif self.year_made < 2012:
                self.price= 250 # heavily-discounted price on machines 10+ years old
            elif self.year_made < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.price = 1000 # recent stuff

            if new_os is not None:
                self.operating_system = new_os # update details after installing new OS
    
    #Functions prints the current price of the computer 
    def check_price(self): 
        print(self.price)
    
    #Function prints all of the details that the computer has including its decription, processor type, hard drive capacity, memory, operating system, year made, and price. 
    def print_product_details(self):
        print("description:", self.description)
        print("Processor Type:", self.processor_type)
        print("Hard Drive Capacity:", self.hard_drive_capacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operating_system)
        print("Year Made:", self.year_made)
        print("Price:", self.price)
       
#Tests for each function
my_my_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
my_my_computer.check_price()
my_my_computer.print_product_details()
my_my_computer.update_price(1300)
my_my_computer.check_price()
my_my_computer.refurbish()
my_my_computer.print_product_details()



   