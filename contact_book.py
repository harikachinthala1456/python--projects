contacts = {}

print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Exit")

choice = input("Enter your choice: ")

if choice == "1":
   name = input("Enter Name: ")
   phone = input("enter Phone Number: ")

   contacts[name] = phone

  print("Contact Added Successfully")

elif choice == "2":
     print(contacts)

elif choice == "3":"
     name = input("Enter name: ")

    if name in contacts:
       print("Phone Number:", contacts[name])
  else:
       print("Contacts Not found")

elif choice == "4":
     name = input("Enter Name: ")

     if name in contacts:
        del contacts[name]
        print("Contact Deleted")
    else:
         print("Contact Not Found")

elif choice == "5":
     print("Thank You")

else:
     print("Invalid Choice")
