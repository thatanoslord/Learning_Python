#pirates flag
#welcoming the guest
#input for choosing doors
#print the result
#print game over

print("""
     ___
     \_/
      |._
      |'."-._.-""--.-"-.__.-'/
      |  \       .-.        (
      |   |     (@.@)        )
      |   |   '=.|m|.='     /
      |  /    .='`"``=.    /
      |.'                 (
      |.-"-.__.-""-.__.-"-.)
      |
      |
      |

       """)
doors = input("""
Welcome to my island!
there are two doors in front of you. 
🚪 a red door, 🚪 a blue door and 🚪 a green door. 
(choose of these three colors): """).lower()
if doors == "red" or doors == "blue" or doors == "green":
    if doors == "red":
        boxes = input("you found three treasure boxes!: white 🎁, yellow 🎁 and brown 🎁. choose one of them. ").lower()
        if boxes == "white":
            print("Oops! you opened a box filled with snakes 🐍🐍🐍.")
        elif boxes == "yellow":
            print("Oops! you opened a box filled with spiders 🕷 ✮☠︎︎.")
        elif boxes == "brown":
            print("Congrats champ, you got the treasure:👑👑👑")
        else:
            print(f"{boxes} isn't one of the choices i gave you")
    elif doors == "blue":
        print("you entred a danger zone run out or you will be killed by the snakes")
    else:
        print("you will be stuck here until you die")
else:
    print(f"the '{doors}' you typed is not in the three choices. choose either 'blue', 'red' or 'green'.")