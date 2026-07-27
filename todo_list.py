tasks = []

print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Exit")

choice = input("Enter your choice: ")


 if choice == "1":
    task = input("Enter a task: ")
    task.append(task)
    print("Task Added Successfully")

 elif choice == "2":
      print(tasks)

 elif choice == "3":
     task = input("Enter task to remove: ")

     if task in tasks:
        tasks.remove(task)
        print("Task Removed Successfully")
    else:
        print("Task Not Found")

elif choice == "4":
     prit("Thank You")

else:
    print("Invalid Choice")
