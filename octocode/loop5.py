all_tasks = input("Enter your tasks for today separated by a coma(,): ").split(", ")
finished_task = []
ongoing_task = []
for task in all_tasks:
    print(task)    
    quest =input (f"did you finish {task} ").lower()
    if quest == "yes":
        print("Good job!")
        finished_task.append(task)
    elif quest == "no":
        print("please don't forget to water them or they will die.")
        ongoing_task.append(task)
    else:
            print("print either 'yes' or 'no'")
    print("-------------------------------------------------")
    
print(f"*********the tasks you have finished are:*********\n{finished_task}\n")
print(f"********* the tasks you are still ongoing :*********\n{ongoing_task}\n")
