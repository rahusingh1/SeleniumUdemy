# Sets
#  {}  unordered | unindexed | no duplicates

my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)

print("Chalk" in my_set)    # true
print("chalk" in my_set)    # false

my_set.add("Pen")
print(my_set)

my_set.update(["Pencil", "Eraser"])
print(my_set)

print(len(my_set))

my_set.remove("Eraser")
print(my_set)
my_set.discard("Pen")
print(my_set)

# my_set.remove("Eraser")     remove will remove the element but through error if element is not present
my_set.discard("Pen")        # discard will remove element but not through error if element not present

my_set.pop()     # it will remove element randomly
my_set.clear()   # it will remove all the elements
print(my_set)

del my_set     # it will delete the entire set

set_2 = {"Apple", 1,2, (3,4,5)}
print(set_2)

# we can also convert list to set
my_list = [1, 2, 3]
print(my_list)
set_3 = set(my_list)
print(set_3)

# in sets we can also do mathematical operations like UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'a', 'b', 'c', 1, 2, 3}
B = {'c', 'd', 3, 4}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)

