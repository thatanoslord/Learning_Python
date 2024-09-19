#enter the name of a book you own : deep work
#enter the of another book you own (or press 'ENTER' to skip): scrum
        #yes = your library: deep work , scrum
#enter the name of a book you wish to have in the future: outlive
#enter the name of another book you wish to have in the future or press 'ENTER' to skip: monday
        #your wishlist : outlive , monday
#enter the name of a book from your wishlist that you have acquired or press 'enter' ti skip: monday
    #your library: deep work scrum monday
    #updated wishlist: outlive
#Enter the name of a book from your library you wish to donate or press 'ENTER' to skip: scrum
        #Final library after donations: deep work, monday

library=[]

firstbook=input("enter the name of a book you own: ").capitalize()
library.append(firstbook)

quest = input("enter the of another book you own (or press 'ENTER' to skip): ").capitalize()
if quest:
        library.append(quest)
        print(f"Your library: {library}")
else:
        print(f"Your library: {library}")

wishlist = []

wish = input("enter the name of a book you wish to have in the future: ").capitalize()
wishlist.append(wish)
wish2 = input("enter the of another book you own (or press 'ENTER' to skip): ").capitalize()
if wish :
        wishlist.append(wish2)
        print(f"your wishlist: {wishlist}")
else:
        print(f"your wishlist: {wishlist}")
        
acquired = input("enter the name of a book from your wishlist that you have acquired or press 'enter' to skip: ").capitalize()
if acquired in wishlist:
        library.append(acquired)
        print(f"your library: {library}")
        wishlist.remove(acquired)
        print(f"updated wishlist: {wishlist}")
else:
        print(f"your library: {library}")
        print(f"updated wishlist: {wishlist}")

donated = input("Enter the name of a book from your library you wish to donate or press 'ENTER' to skip: ").capitalize()
if donated in library:
        library.remove(donated)
        print(f"Final library after donations: {library}")
else:
        print(f"Final library after donations: {library}")