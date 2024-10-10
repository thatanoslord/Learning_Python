#creating an input that says to enter full name separated by a coma
names = input("Enter The first and last name of your friends separated by a coma: ").split(", ")
first_letter=[]
separator=".\n"
for i in range(len(names)):
    i = names[i].split(" ")
    first_letter.append(f"{i[0][0]}.{i[1][0]}") 
    print(i)
print(separator.join(first_letter)) 

