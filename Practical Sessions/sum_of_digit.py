# digit = input("Enter the digits :")

# sum = 0

# for i in range (digit , )


num =abs(int(input("Enter the number: ")))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)
