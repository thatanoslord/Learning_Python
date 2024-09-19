colors=[]
choice = input("add you first color: ")
colors.append(choice)
sec_choice = input("do you want to add another color 'Yes' or 'No': ").lower()
if sec_choice == "yes":
    sec_color = input("add another color: ")
    colors.append(sec_color)
    print(colors)
elif sec_choice == "no":
    print(colors)
else: 
    print("Please enter either 'YES' or 'No'.")