#print the odd numbers table in between 1 to 10

for i in range(1, 10):  #goes from 1 to 9
    if i % 2 !=0:  # odd num condition
        for j in range (1,11):  # to print the table till 10 
            print(i*j) 
        print()
