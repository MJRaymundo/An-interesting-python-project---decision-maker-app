# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Instructions: Create an interesting/exciting python project/program taking inspiration from a youtube video. Create a demo and present an idea on where you can apply what you created.
# Idea: An app that helps make you decisions. Video link: https://www.youtube.com/watch?v=_xf1TMs0ysk from Tina Huang
# Reason for choosing: A game I currently play has a gameplay feature of a crafting system, I want to create an app that would help me make a decision based on a few factors.
# Taking in user input
ResourceNameDict = ['Ore', 'Wood', 'Fiber', 'Stone', 'Hide']
ResourceTierDict = {'2.0' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '3.0' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '4.0' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '4.1' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '4.2' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '4.3' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '5.0' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '5.1' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '5.2' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '5.3' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '6.1' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '6.2' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '6.3' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '7.1' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '7.2' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '7.3' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '8.1' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '8.2' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}, '8.3' : {'Profit' : 0, 'SellVolume' : 0, 'DailyLimit' : 0, 'BuyVolume' : 0}}
ResourceDictionary = dict.fromkeys(ResourceNameDict, ResourceTierDict)
def add_item():
    while True:
        try:
            ResourceName = str(input("Input resource Name :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            ResourceTier = str(input("Input resource Tier :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            ResourceFactor = str(input("Input resource Factor :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            if ResourceFactor.upper() == 'PROFIT':
                ProfitInput = int(input("Input Profit :"))
                ResourceDictionary[ResourceName][ResourceTier][ResourceFactor] = ProfitInput
            elif ResourceFactor.upper() == 'SELLVOLUME':
                SellVolumeInput = int(input("Input SellVolume :"))
                ResourceDictionary[ResourceName][ResourceTier][ResourceFactor] = SellVolumeInput
            elif ResourceFactor.upper() == 'DAILYLIMIT':
                DailyLimitInput = int(input("Input Profit :"))
                ResourceDictionary[ResourceName][ResourceTier][ResourceFactor] = DailyLimitInput
            elif ResourceFactor.upper() == 'BUYVOLUME':
                BuyVolumeInput = int(input("Input Profit :"))
                ResourceDictionary[ResourceName][ResourceTier][ResourceFactor] = BuyVolumeInput
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    main_menu()
# Proccessing of data
def decision_maker():
    while True:
        try:
            DecisionResourceName = str(input("What type of resource do you want to filter? :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            DecisionResourceFactor = str(input("What factor do you want to filter it by? :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    PrimaryFilter = {key: max(DecisionResourceFactor.values()) for key, DecisionResourceFactor in ResourceDictionary[DecisionResourceName].items()}
    BestResource = max(zip(PrimaryFilter.values(), PrimaryFilter.keys()))
    # Displaying of result
    print(DecisionResourceName + ' filtered by ' + DecisionResourceFactor + ' = (Value, Resource Tier)', BestResource)
    main_menu()
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