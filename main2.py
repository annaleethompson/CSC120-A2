from computer import Computer
from oo_resale_shop import ResaleShop, computer
def main(): 
    
    itemID = 0

    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    print("Buying", computer)
    print("Adding to inventory...")
    computer_id = ResaleShop.buy(computer, itemID)
    print("Done.\n")

    print("Checking inventory...")
    ResaleShop.print_inventory(itemID)
    print("Done.\n")

    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    Computer.refurbish(computer_id, new_OS)
    print("Done.\n")

    print("Checking inventory...")
    ResaleShop.print_inventory()
    print("Done.\n")

    print("Selling Item ID:", computer_id)
    ResaleShop.sell(computer_id)

    print("Checking inventory...")
    ResaleShop.print_inventory()
    print("Done.\n")

if __name__ == "__main__": main()

