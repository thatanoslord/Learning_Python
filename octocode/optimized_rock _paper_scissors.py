#welcoming
print("Welcome to The Rock, Paper, Scissors game ")

#the input to start the game or to give instruction:
start = input("Please Click 'Enter' to start or print 'help' for the rules: ").lower()
    #instructions
if start == "help":
    print("""
          *********** RULES ***********
          1) You choose and the computer chooses
          2) Rock smaches the Scissors -> Rock wins
          3) Scissors cut the Paper -> Scissors win
          4) Paper covers Rock -> Paper wins 
          5) If you choose the same as the computer you Draw
          """)
#importing random file and making a list that contain the three words:
import random
mylist = ["Rock", "Paper", "Scissors"]
mylist[0] = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
mylist[1] ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
mylist[2] = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

        """
#input to let the  user to print what he 
choose = input("Enter your choice (Rock, Paper , Scissors): ").capitalize()
computer = random.choice(mylist)
if choose == "Rock" or choose=="Paper" or choose== "Scissors":
    if computer: 
        if computer == mylist[0] and choose == "Rock":
            print(f"You chose:\n{mylist[0]}\ncomputer chose:\n{mylist[0]}\n You draw")
        elif computer == mylist[0] and choose == "Paper":
            print(f"You chose:\n{mylist[1]}\ncomputer chose:\n{mylist[0]}\n You Won")
        elif computer == mylist[0] and choose == "Scissors":
            print(f"You chose:\n{mylist[2]}\ncomputer chose:\n{mylist[0]}\n You lose") 
    elif computer:
        if computer == mylist[1] and choose == "Rock":
            print(f"You chose:\n{mylist[0]}\ncomputer chose:\n{mylist[1]}\n You lose")
        elif computer == mylist[1] and choose == "Paper":
            print(f"You chose:\n{mylist[1]}\ncomputer chose:\n{mylist[1]}\n You draw")
        elif computer == mylist[1] and choose == "Scissors":
            print(f"You chose:\n{mylist[2]}\ncomputer chose:\n{mylist[1]}\n You won")
    elif computer:
        if computer == mylist[2] and choose == "Rock":
            print(f"You chose:\n{mylist[0]}\ncomputer chose:\n{mylist[2]}\n You won")
        elif computer == mylist[2] and choose == "Paper":
            print(f"You chose:\n{mylist[1]}\ncomputer chose:\n{mylist[2]}\n You lose")
        elif computer == mylist[2] and choose == "Scissors":
            print(f"You chose:\n{mylist[2]}\ncomputer chose:\n{mylist[2]}\n You draw")
else: 
    print(" Please use either Rock, Paper, or Scissors")

