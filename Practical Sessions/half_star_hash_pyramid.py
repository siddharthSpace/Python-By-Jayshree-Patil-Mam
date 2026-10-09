
n = int(input("Enter how many rows: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print("*" * i)
    else:
        print("#" * i)

    # for j in range (1 ,i+1) 