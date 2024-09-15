nationality = input("are you Moroccan? print 'Yes' or 'No'\n"  ).lower()
if nationality.lower() == "yes":
    print("good, that's the first step")
    
    is_18 = input("are you 18 or above? 'Yes' or 'No' : ").lower()
    if is_18 == "yes":
        print("You apply for your ID.")
    elif is_18 == "no":
        print("Sorry, you can't have an ID because you are not old enough.")
    else:
        print(f"Sorry, '{is_18}' isn't in the choices you have to write either 'Yes' or 'No'")
else:
    print("Sorry, because you are not Moroccan you can't apply for the ID.")