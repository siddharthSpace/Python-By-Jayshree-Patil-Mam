# counting the vowels in the string

text = input("Enter a string: ")
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
