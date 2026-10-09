# a = [10 ,"siddharth", 25 , "vedang", 40 , "sumit"]
# highest = max(x for x in a if type(x) == int)
# i = a.index(highest)
# print(a[:i])
# print(a[i:])


a = [10 ,"siddharth", 25 , "vedang", 40 , "sumit" , 30 ,"vedant", 44 , "avdhut"]
highest = max(x for x in a if type(x) == int)
i = a.index(highest)
print(a[:i])
print(a[i:])


data = [10, 20, "Siddharth", "Rahul", 30]
data.append("Sumit")
data.append("Vedang")

#  3rd highest number
numbers = [x for x in data if isinstance(x, int)]
numbers.sort(reverse=True)

print("Updated list:", data)
print("3rd highest number:", numbers[2])
