quest = input("Enter the names of attendees separated with coma(,): ")
person =[]
person.extend(quest.split(", "))
for x in person:
    print(x)
    response =input ("Is this person attending(Yes/No)").capitalize()
    if response == "Yes":
        print("This person is confirmed")
        print("-------------------------------")
    elif response == "No":
        print("This person is not confirmed")
        print("-------------------------------")
    else:
        print("Please type either (Yes or No)")