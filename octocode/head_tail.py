print("Welcome to the Coin Guessing Game!")
choose = int(input("Choose a method to toss the coin: "))
import random
if choose == 1:
    randomness = random.random()
    if randomness >= 0.5:
        randomness = "head"
    else :
        randomness = "tail"
    head_tail = input("your Guess (Head or Tail): ").lower()
    if randomness ==head_tail:
        print("You won")
    elif randomness != head_tail: 
        print("You lost")
    else:
        print("please print either Head or Tail.")
elif choose == 2:
    randomness2 = random.randint (1,2)
    if randomness2 ==1:
        randomness2 = "head"
    else:
        randomness2 = "tail"
    
    head_tail2 = input("your Guess (Head or Tail):").lower()
    if head_tail2 ==randomness2 :
        print("You won")
    elif head_tail2 != randomness2:
        print(f"You lost")
    else:
        print("Please enter either Head or tail.")
else:
    print("Please choose either 1 or 2")
