
print("********* Welcome to iShop calculator *********\n")

items=int(input("How many items are there in your basket today? "))
basket= []
whole_price=[]
if items > 0:
    print("\nlet's get to count them....\n")

    for i in range(1,items+1):
        item=input(f"\nplease tell me the name of the item number {i}, give it's name: ")
        basket.append(item)

        price = float(input(f"\nwhat is the price of the {item}: "))
        whole_price.append(price)

    quest=input("would like to see your entire basket items?(Yes or no): ").lower()
    if quest == "yes":
        print(f"\nthis is your basket {basket}")
    else:
        print("\nClick enter to continue: ")

    basket2 = input("\nwould you like to see how much it 'll cost? (yes or no): ")
    if basket2=="yes":
        print(f"it will cost you {sum(whole_price)} $") 
    else:
        input("Please press Enter to exit: ")
else:
    print("I guess you're not in the mood to buy something")