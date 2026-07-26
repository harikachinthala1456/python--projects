number = int(input("Enter a decimal number: "))

binary = ""

while number > 0:
     remainder =  number % 2
     binary = str(reaminder) + binary
     number = number // 2

print("Binary =", binary)
