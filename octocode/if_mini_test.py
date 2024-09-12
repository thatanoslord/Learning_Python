#first project 
password = input("enter you password: ")
if password == "abc":
    print("The password is correct.")
else:
    print("the password is wrong. try again\n")
print("========================================")
#second project
words = input("Please enter: ")
if words == "yes":
    print("you wrote yes.")
elif words == "no":
    print("you wrote no.")
elif words == "maybe":
    print("you wrote maybe.")
else :
    print(f"You typed '{words}' which is not an option, please repeat again")
#third project:
number = int(input("Guess the number:"))
if number == 7:
    print("you guessed the right number")
else:
    print("you guessed the wrong number")
 

    