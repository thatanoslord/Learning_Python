print("Can you drive in morocco?")
age=int(input("how old are you? : "))
license = input("Do you have a license? : ")
if age >= 18 and license.lower() == "yes":
    print("Yes, you can drive in Morocco")
else:
    print("Sorry, you can't drive")