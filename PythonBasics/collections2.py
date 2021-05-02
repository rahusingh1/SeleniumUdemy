# Tuple
# Tuple are ordered | indexed | unchangeable | duplicates

my_tuple = ("Apple", "Grapes", "Oranges")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:3])      # it will print the element in range from 0 to 2

for val in my_tuple:
    print(val)

# my_tuple[1] = "Banana"       TypeError: 'tuple' object does not support item assignment
# del my_tuple[2]            TypeError: 'tuple' object doesn't support item deletion
# del my_tuple               It will delete the entire tuple

print(len(my_tuple))

# we can also add multiple data type to a tuple
tuple_2 = ("Mango", (1,2,3), ["Torrento", "New Delhi"])
print(tuple_2)
print(tuple_2[2][1])

tuple_2[2][0] = "New York"   # tuple not changeable but list is so we are able to change list element here
print(tuple_2)

print("Mango" in tuple_2)  # true
print("Banana" in tuple_2) # false

