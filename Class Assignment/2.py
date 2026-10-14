# Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

with open("2nd_4th.txt", "r") as file:
    lines = file.readlines()

print("number of lines:", len(lines))

print("2nd line:", lines[1])
print("4th line:", lines[3])
