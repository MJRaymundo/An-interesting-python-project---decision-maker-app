# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Instructions: Create an interesting/exciting python project/program taking inspiration from a youtube video. Create a demo and present an idea on where you can apply what you created.
# Idea: An app that helps make you decisions. Video link: https://www.youtube.com/watch?v=_xf1TMs0ysk from Tina Huang
# Reason for choosing: A game I currently play has a gameplay feature of a crafting system, I want to create an app that would help me make a decision based on a few factors.
# Taking in user input
ResourceDictionary = {}
FactorValue = ""
ResourceName = ""
ResourceTier = ""
ResourceFactor = ""
def add_item():
    while True:
        try:
            ResourceName = str(input("Name of resource? :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            ResourceTier = str(input("Tier and enchantment of resource? :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            ResourceFactor = str(input("Which resource factor? :"))
            if ResourceFactor.upper() == "PROFIT":
                FactorValue = int(input("Enter profit percentage: "))
            elif ResourceFactor.upper() == "SELLVOLUME":
                FactorValue = int(input("Enter sell volume: "))
            elif ResourceFactor.upper() == "DAILYLIMIT":
                FactorValue = int(input("Enter daily limit: "))
            elif ResourceFactor.upper() == "BUYVOLUME":
                FactorValue = int(input("Enter buyvolume: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
# Name of resource/item // Ore, Wood, Fiber, Stone, Hide //, Tier + Enchantment // T2.0 - T8.3 //, Factors that will affect the decision // Proft, SellVolume, DailyLimit, BuyVolume //
def store_data():
    ResourceDictionary ={
        ResourceName : 
        {
            ResourceTier : 
            {
                ResourceFactor : FactorValue
            }
        }
    }
    print(ResourceDictionary)
    print(ResourceName, ResourceTier, ResourceFactor, FactorValue)
# ResourceTierDictionary[ResourceTier] = {ResourceTier : 2.0, 3.0, 4.0, 4.1, 4.2, 4.3, 5.0, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3}
# ResourceFactor : Proft, SellVolume, DailyLimit, BuyVolume
# Proccessing of data
def decision_maker():
    str(input("What type of resource? "))
    str(input("What tier and enchantment of the resource? "))
    str(input("By which resource factor would you like to filter it by?"))
    
# Displaying of result
# Simple Menu
def exit():
    exit_input = str(input("Exit? (Y/N)"))
    while True:
        if exit_input.upper() == "N":
            main_menu()
        elif exit_input.upper() == "Y":
            quit()
        else:
            print("Invalid input.")
            exit()

def main_menu():
    print("Menu: ")
    print("      1 -> Add an entry. ")
    print("      2 -> Decide on a resource. ")
    print("      3 -> Exit. ")
    user_input = input("Enter the number of the function you want to use: ")
    while True:
            if user_input == "1":
                add_item()
            elif user_input == "2":
                decision_maker()
            elif user_input == "3":
                exit()
            else:
                print("Invalid input.")
                main_menu()

main_menu()