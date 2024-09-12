total_second = int(input("Type the number of seconds: \n"))
hours = total_second // 3600
minutes_left = (total_second % 3600) // 60
second_left = total_second % 60
print(f"{total_second} seconds is equivalent to : {hours} hours, {minutes_left} minutes and {second_left}" )