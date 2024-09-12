age = int(input("How old are you? "))
license = input("do you have a license? prent either (Yes) or (No): ")
if age >= 18 and license.lower() == "yes":
    print("you can drive")
elif age < 18 or license.lower == "no":
    print("Sorry, You can't drive")
else:
    print(f"sorry entry of ({license}) is not understod ")