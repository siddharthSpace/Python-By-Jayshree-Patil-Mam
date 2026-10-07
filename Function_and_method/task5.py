#Create a list of 10 numbers and display the sum of last four elements

#Remove the items form the list located at 2nd and 5th position

#Print the difference of highest and smallest number in the list

#Append a new element in the list which is half of the item of 3rd position 


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sum_last_four = sum(numbers[-4:])
print("Sum of last four elements:", sum_last_four)

numbers.pop(4)
numbers.pop(1)

print("List after removing :", numbers)


difference = max(numbers) - min(numbers)
print("Difference between numbers:", difference)


third_item = numbers[2]
numbers.append(third_item / 2)

print("Final list:", numbers)