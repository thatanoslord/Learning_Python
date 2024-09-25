basket = [["Apples", "Bananas"],["Milk", "Water"]]
print(basket)
input("Press Entre to change the content: .......")
number = [1, 2, 3]
basket.append(number)
basket[0].insert(0, "Oranges")
basket[0].append("Kiwis")
basket[1].append("Tea")
basket[1].insert(0,"Coffee")
basket[1].remove("Water")


print(basket)