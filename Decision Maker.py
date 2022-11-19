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
            ResourceName = str(input("Input Name :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            ResourceTier = str(input("Input Tier :"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    while True:
        try:
            ResourceFactor = str(input("Input Factor :"))
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

#    while True:
#        try:
#            SellVolumeInput = int(input("Input SellVolume :"))
#        except ValueError:
#            print("Invalid input.")
#            continue
#        else:
#            break
#    while True:
#        try:
#            DailyLimitInput = int(input("Input DailyLimit :"))
#        except ValueError:
#            print("Invalid input.")
#            continue
#        else:
#            break
#    while True:
#        try:
#            BuyVolumeInput = int(input("Input BuyVolume :"))
#        except ValueError:
#            print("Invalid input.")
#            continue
#        else:
#            break
    print(ResourceDictionary[ResourceName][ResourceTier][ResourceFactor])
#    max_value, max_key = max(((v,k) for inner_d in ResourceDictionary.values() for k,v in inner_d.items()))
#    print("This is the result ",max_value, max_key)
#    ResourceDictionary = dict(
#        Ore = {'2.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '3.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.3' : [Profit, SellVolume, DailyLimit, BuyVolume]},
#        Wood = {'2.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '3.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.3' : [Profit, SellVolume, DailyLimit, BuyVolume]},
#        Fiber = {'2.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '3.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.3' : [Profit, SellVolume, DailyLimit, BuyVolume]},
#        Stone = {'2.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '3.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.3' : [Profit, SellVolume, DailyLimit, BuyVolume]},
#        Hide = {'2.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '3.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '4.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.0' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '5.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '6.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '7.3' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.1' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.2' : [Profit, SellVolume, DailyLimit, BuyVolume], '8.3' : [Profit, SellVolume, DailyLimit, BuyVolume]}
#    )
    main_menu()
#    while True:
#        try:
#            ResourceFactor = str(input("Which resource factor? :"))
#            if ResourceFactor.upper() == "PROFIT":
#                FactorValue = input("Enter profit percentage: ")
#            elif ResourceFactor.upper() == "SELLVOLUME":
#                FactorValue = input("Enter sell volume: ")
#            elif ResourceFactor.upper() == "DAILYLIMIT":
#                FactorValue = input("Enter daily limit: ")
#            elif ResourceFactor.upper() == "BUYVOLUME":
#                FactorValue = input("Enter buyvolume: ")
#        except ValueError:
#            print("Invalid input.")
#            continue
#        else:
#            break

#    ResourceDictionary[ResourceName] ={
#        ResourceName : 
#        {
#            ResourceTier : 
#            {
#                ResourceFactor : FactorValue
#            }
#        }
#    }
#    print(ResourceName,ResourceTier, ResourceFactor, FactorValue)
# Name of resource/item // Ore, Wood, Fiber, Stone, Hide //, Tier + Enchantment // T2.0 - T8.3 //, Factors that will affect the decision // Proft, SellVolume, DailyLimit, BuyVolume //
    
#    print(ResourceDictionary)
#    print(ResourceName, ResourceTier, ResourceFactor, FactorValue)
# ResourceTierDictionary[ResourceTier] = {ResourceTier : 2.0, 3.0, 4.0, 4.1, 4.2, 4.3, 5.0, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3}
# ResourceFactor : Proft, SellVolume, DailyLimit, BuyVolume
# Proccessing of data
def decision_maker():
#    print(ResourceDictionary, ResourceDictionary.get("Ore"))
    FactorValue = ResourceDictionary.values()
    BestResource = max(FactorValue)
    print('The best resource to craft is :', BestResource)

# ResourceDictionary[ResourceName[ResourceTier[ResourceFactor[FactorValue]]]]
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