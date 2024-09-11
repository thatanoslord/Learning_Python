total_second = input("Type the number of seconds: \n")
minutes = int(total_second) // 60
left_sec = int(total_second) % 60
hours = minutes // 60
left_min = minutes % 60
print("This course is:", hours, "hours, ", left_min, "minutes and ", left_sec, "seconds long" )