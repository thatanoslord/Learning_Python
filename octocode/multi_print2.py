print("let's see if you were originated from Agadir.")
agadir = input("Which town is located in Agadir 'Ain choq', 'Taddart' or 'Derb ghalef': ").lower()
if agadir == "ain choq":
    print(f"Oops {agadir} is not located in Agadir so You are not Agadiri fella.")
elif agadir == "taddart":
    print(f"Yes {agadir} is in north part of Agadir near to Anza, but we will have other questions to now if really you were Agadirian:") 
    transport = input("What do we use if we want to get to Taddart is it 'Teleferique', 'Indrive' or 'Khettaf': ").lower()
    if transport == "teleferique" or transport == "indrive" or transport == "khettaf":
        if transport ==  "teleferique":
            print(f"Oops, {transport} is not used by taddart fellas")
        elif transport == "indrive":
            print(f"Oops, {transport} is not used by taddart fellas")
        elif transport == "khettaf":
            print(f"Yes, {transport} is the most this that taddarties are using for transportation:")
    else:
        print(f"{transport} is not in the choices.")
elif agadir == "Derb ghalef":
    print(f"Oops {agadir} is not located in Agadir so You are not Agadiri fella.")
else:
    print(f"Sorry {agadir} is not one of the choises I gave you")