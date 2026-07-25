number = int(input("Enter a positive number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial =", factorial)
