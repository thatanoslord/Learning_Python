#welcome to 'whose wallet?'
#you will give me a lis of names, and I will pick a person to pay
#If you are radu, enter the names separated by a coma(, ):
#Please ask "Ibrahim" to take his wallet out. Dinner is on him

print("welcome to 'whose wallet?': ")

wallet = []
import random

names = input("you will give me a lis of names, and I will pick a person to pay: ")
wallet = names.split(", ")
number = len(wallet) -1
number = random.randint(0,number)
print(f"Please, ask {wallet[number]} to take his wallet out. Dinner is on him.")

 