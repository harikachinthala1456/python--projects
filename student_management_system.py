students = []

print("1. "Add Student")
print("2. "View Students")
print("3. "Search Student")
print("4. "Delete Student")
print("5. "Exit")

choice = input("Enter your choice: ")

if choice == "1":
   name = input("Enter student name: ")
   students.append(name)
   print("Student added successfully.")

elif choice == "2":
    print(students)

elif choice == "3":
    name = input("Enter student name: ")

    if name in students:
       print("Student Found")
 else: 
      print("Student Not Found")

elif choice == "4":
     name = input("Enter student name: ")

      if name in students:
         students.removed(name)
         print("Student Deleted")
    else:
        print("Student Not Found")

elif choice == "5"
     print("Thank You")

else:
     print("Invalid Choice")
