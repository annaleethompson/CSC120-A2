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
    def __init__(item, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        item.descrip = description
        item.proctype = processor_type
        item.harddrive = hard_drive_capacity
        item.memory = memory
        item.operatingsyst = operating_system
        item.year = year_made
        item.price = price
        
    # What methods will you need?
        #storing information about a specific computer
        #updating a computer's OS

    def create_computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }