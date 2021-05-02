
if 5 > 3:
    print("5 is greater than 3")

num = 10
if num > 0:
    print("this is a positive no")
elif num == 0:
    print("Num is Zero")
else:
    print("this is a negative no")

# list in python is as follows
list = [1, 2, 3, 4, 5]
sum = 0
for val in list:
    print(val)
    sum = sum+val
print("list total is ", sum)

fruits = ["Mango", "Banana", "Papaya"]

for val in fruits:
    print(val)
else:
    print("No fruits left")

num = 10
sum = 0
i = 1

while i < num:
    sum = sum + i
    i = i + 1
print("Total is ", sum)