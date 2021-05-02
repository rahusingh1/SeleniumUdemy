# There are 4 collection data types in python | List | Tuple | Set | Dictionary
# Collections are data types where we store array of elements
# LIST : we can create list using square brackets
# lists are ordered | indexed | changeable | duplicates
my_list = ["New Delhi", "Mainpuri", "Gurgaon"]

print(my_list)
print(my_list[1])

my_list[2] = "New York"     # elemets are  changeable, here we are changing element of index 2
print(my_list)

for val in my_list:
    print(val)

print(len(my_list))   # print the length of the list

my_list.append("Tokyo")
print(my_list)

my_list.insert(1, "Singapore")
print(my_list)

my_list.remove("Mainpuri")
print(my_list)

# pop can be used in two ways :
# 1. pop without any index position : it will popup and remove the last element
# 2. pop with index position : it will remove the indexed position element
my_list.pop()
print(my_list)
my_list.pop(2)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()       # it will clear the list items from the list
print(my_list)

fruits = ["Apple", "Banana", "Mango", "Oranges"]
print(fruits)
fruits.reverse()
print(fruits)

# we could also create a list with multiple data types
list_2 = ["Oranges", 1,2.2,3.0]
print(list_2)
list_3 = ["Apple", [1,2,3], 5.6, ['a','b','c']]
print(list_3)
print(list_3[1][1])
print(list_3[3][2])

