print("**** Welcome to the multiplication table ****")
number= int(input("Please enter a number: "))
print(f"Multiplication table for {number}")
for i in range(1,11):
    result = number * i
    print(f"{number} x {i}= {result}")