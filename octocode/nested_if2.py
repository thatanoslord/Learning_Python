print("We have a deal for you:")
nationality = input("Are you Moroccan type 'yes' or 'no'? : ").lower()
if nationality == "yes":
    print("Now you can get to the next step")
    
    city=input("In which city do you live in 'Casablanca', 'Agadir', 'Marrakesh' or 'Rabat'? (choose one of these 4 cities) :" ).lower()
    if city == "agadir" or city == "casablanca" or city =="rabat" or city=="marrakesh":
        print(f"Now you can visit our Head quarter in {city}.") 
    else:
        print(f"sorry we don't have a Head quarter your {city} till now stay connected in  our platform so you can get our news and events.")
elif nationality == "no":
    print("Sorry, this program is only for the Moroccan community.")
else:
    print(f"you typed {nationality} and this isn't one of choices of this question.\nPlease type either 'Yes' or 'No'.")