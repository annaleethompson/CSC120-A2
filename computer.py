from typing import Optional

class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
        
    # What methods will you need?
        #storing information about a specific computer
        #updating a computer's OS

    def update_price(self, new_price):
            self.price = new_price

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
    
    def check_price(self): 
        print(self.price)
    
    def print_product_details(self):
        print("description:", self.description)
        print("Processor Type:", self.processor_type)
        print("Hard Drive Capacity:", self.hard_drive_capacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operating_system)
        print("Year Made:", self.year_made)
        print("Price:", self.price)
       
#Tests
# my_my_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
# my_my_computer.check_price()
# my_my_computer.print_product_details()
# my_my_computer.update_price(1300)
# my_my_computer.check_price()
# my_my_computer.refurbish()
# my_my_computer.print_product_details()



   