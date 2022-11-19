# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Instructions: Create an interesting/exciting python project/program taking inspiration from a youtube video. Create a demo and present an idea on where you can apply what you created.
# Idea: An app that helps make you decisions. Video link: https://www.youtube.com/watch?v=_xf1TMs0ysk from Tina Huang
# Reason for choosing: A game I currently play has a gameplay feature of a crafting system, I want to create an app that would help me make a decision based on a few factors.
# Taking in user input
ResourceDictionary = {}
Profit = "SampleP"
SellVolume = "SampleS"
DailyLimit = "SampleD"
BuyVolume = "SampleB"
while True:
    try:
        ResourceName = str(input("What type of resource do you want to craft? :"))
    except ValueError:
        print("Invalid input.")
        continue
    else:
        break
while True:
    try:
        ResourceTier = str(input("What tier and enchantment of the resource? :"))
    except ValueError:
        print("Invalid input.")
        continue
    else:
        break
while True:
    try:
        ResourceFactor = str(input("What factor would you like to filter it out from? :"))
    except ValueError:
        print("Invalid input.")
        continue
    else:
        break

while True:
    if ResourceFactor.upper() == "PROFIT":
            print(1)
            break
    elif ResourceFactor.upper() == "SELLVOLUME":
            print(2)
            break
    elif ResourceFactor.upper() == "SELLVOLUME":
            print(3)
            break
    elif ResourceFactor.upper() == "BUYVOLUME":
            print(4)
            break
    else:
        print("Invalid input.")
        break

# Name of resource/item // Ore, Wood, Fiber, Stone, Hide //, Tier + Enchantment // T2.0 - T8.3 //, Factors that will affect the decision // Proft, SellVolume, DailyLimit, BuyVolume //
ResourceDictionary ={
    ResourceName : 
    {
        ResourceTier : 
        {
            ResourceFactor : [Profit, SellVolume, DailyLimit, BuyVolume]
        }
    }
}
print(ResourceDictionary)
print(ResourceName, ResourceTier, 'by' + ResourceFactor,)
# ResourceTierDictionary[ResourceTier] = {ResourceTier : 2.0, 3.0, 4.0, 4.1, 4.2, 4.3, 5.0, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3}
# ResourceFactor : Proft, SellVolume, DailyLimit, BuyVolume
# Proccessing of data
# Displaying of result