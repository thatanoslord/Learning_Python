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
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

        """
#input to let the  user to print what he 
choose = input("Enter your choice (Rock, Paper , Scissors): ").capitalize()
if choose == "Rock" or choose == "Paper" or choose == "Scissors": 
    computer = random.randint(0,2)
    if computer ==0:
        computer = "Rock"
        if choose == "Rock":
            print(f"""You chose:
                  {rock}
                  computer chose
                  {rock}
                  draw""")
        elif choose == "Paper":
            print(f"""You chose:
                  {paper}
                  computer chose
                  {rock}
                  you won""")
        else:
            print(f"""You chose:
                  {scissors}
                  computer chose
                  {rock}
                  you lost""")
    elif computer == 1:
        computer = "Paper"
        if choose == "Rock":
            print(f"""You chose:
                  {rock}
                  computer chose
                  {paper}
                  you lost""")
        elif choose == "Paper":
            print(f"""You chose:
                  {paper}
                  computer chose
                  {paper}
                  you draw""")
        else:
            print(f"""You chose:
                  {scissors}
                  computer chose
                  {paper}
                  you won""")
    else:
        computer = "Scissors"
        if choose == "Rock":
            print(f"""You chose:
                  {rock}
                  computer chose
                  {scissors}
                  you won""")
        elif choose == "Paper":
            print(f"""You chose:
                  {paper}
                  computer chose
                  {scissors}
                  you lost""")
        else:
            print(f"""You chose:
                  {scissors}
                  computer chose
                  {scissors}
                  you draw""")
else:
    print("Invalid choice. Please run the program again and Choose Rock, Paper, or Scissors.")