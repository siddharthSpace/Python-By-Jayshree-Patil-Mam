# spliting the string form the center 


text = input("Enter a string: ")

middle = len(text) // 2
first_half = text[:middle]
second_half = text[middle:]

print("First half:", first_half)
print("Second half:", second_half)
