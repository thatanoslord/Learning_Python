attendees=["Alice", "John", "ken", "Moussa"]
for person in attendees:
    print(person)
    quest= input("Is this person attending? (yes/no): ").lower()
    if quest == "yes":
        print("Attendance is Confirmed!")
    elif quest == "no":
        print("Attendance is not confirmed.")
    else:
        print("Please use (Yes/No).")
