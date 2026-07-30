balance = 1000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
   amount = float(input("Enter deposit amount: "))
   balance = balance + amount
   print("Updated Balance =", balance)

elif choice == "2":
     amount = float(input("Enter withdrawal amount: "))

     if amount <= balance:
        balance = balance - amount
        print("Updated Balance =", balance)
   else:
       print("Insufficient Balance")

elif choice == "3":
     print("Current Balance =", balance)

elif choice == "4":
     print("Thank You")

else:
    print("Invalid Choice")
