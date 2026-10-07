text = " Welcome to IMCC !"

#1 . Strip spaces form both lowercase


# 4 . Capitalize first letter
text = text.strip()
print("Captalize first Letter :", text.capitalize())

# 5 . Title case (capitalize each word)

print(text.title())

# 6 . Count occurences of a substring 

print("Lower C occurs :", text.count("C"), "times in text")

#7 . find the position of a substring(-1 if not found)

print("position of IMCC in text is  ", text.find("IMCC"))


#8 Replace a substring
print(text.replace("IMCC", "Python Magic"))

#9 Check if string starts or ends with certain substring
print(text.startswith(" We"))
print(text.endswith("! "))

#10 spit sting into list by a delimiter 
print("Simple split ", text.split())

#11 join a list of strings with a separator
word = ["Python", "is", "fun"]
print(" ".join(word))