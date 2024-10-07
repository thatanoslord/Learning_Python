#range has three methods :
#the first one range can get only stop value example: range(stop): as an exp range(3) = 0 1 2 "i" here stop without writing the stop value
#the second one range can use the start and stop as a vlaue: range (star, stop) as an exp range(1, 3) = 1 2 here it starts from the value 1 but stops before 3
#the third method is range can use steps which means you give how it counts, range(start, stop, step) as an exp range (0,10,2) = 0 2 4 6 8 .
for i in range(10):
    print(i)
print("\n-------------------------")
for i in range(1,10):
    print(i) 
print("\n-------------------------")   
for i in range(0,10,2):
    print(i)
print("\n-------------------------")