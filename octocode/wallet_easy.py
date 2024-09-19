#welcome to 'whose wallet?'
#you will give me a lis of names, and I will pick a person to pay
#If you are radu, enter the names separated by a coma(, ):
#Please ask "Ibrahim" to take his wallet out. Dinner is on him
import random
print("welcome to 'whose wallet?'")
names = input("you will give me a lis of names, and I will pick a person to pay If you are ready, enter the names separated by a coma(, ): ").split(", ")
print(f"Please ask '{random.choice(names)}' to take his wallet out. Dinner is on him")