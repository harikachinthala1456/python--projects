number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))

operations = input( "Enter operation (+,-,*,/):")

if operation == "+":
   print("Answer =", num1 + num2)

elif operation == "-":
   print("Answer=", num1 - num2)

elif operation == "*":
    print("Answer=",num1 * num2)

elif operation == "/": 
     if num2 != 0:
     print("Answer=",num1 / num2)
else:
     print("Cannot divisible by zero")

else:
     print(Invalid operation")
  
  
