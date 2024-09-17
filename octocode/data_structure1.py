colors = []
first_color = input("add the first color you like: ")
colors.append(first_color)
quest = input("Do you want to  add more colors? Yes, or No? ").lower()
if quest == "yes":
    second_color = input("Add another color to the list: ")
    colors.append(second_color)
    print(colors)
elif quest == "no":
    print(f"{colors}")
else:
    print("Please, Choose either Yes or No.")