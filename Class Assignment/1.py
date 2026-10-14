# Write a program too read a file and count how many vowels are present in its content.

with open("count_vowels.txt", "r") as file:
    content = file.read()

count = 0

for ch in content:
    if ch.lower() in "aeiouAEIOU":
        count += 1

print("Total vowels:", count)
