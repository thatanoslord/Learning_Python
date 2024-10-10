numbers= [1,2,3,4,5]
total=0
print("let's sum the numbers from 1 to 5")
for i in range(len(numbers)):
    print(f"-> {i+1}")
    total += numbers[i]
    print(f"current Total: {total}")
print(f"total: {total} \n")