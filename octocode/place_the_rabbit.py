#entrance to the game 
print("Welcome to place the rabbit")
place = [["🌱", "🌱", "🌱"],["🌱", "🌱", "🌱"],["🌱", "🌱", "🌱"]]
print(f"""
      {place[0]}
      {place[1]}
      {place[2]}
      """)
#the user enters row and column
print("where should The rabbit go? 🐇")
position = input("please enter row and column so the rabbit can get the carrots: ")

#indexing the position of the input
row = int(position[0])
column = int(position[1])

#using the indexing inside the place so can be changer to the rabbit
place[row - 1][column -1] = '🐇' 

print(f"""
      {place[0]}
      {place[1]}
      {place[2]}
      """)
