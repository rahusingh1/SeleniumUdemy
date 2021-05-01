print("Hello World!!")

#variables
#variables are case sensitive
# in variable naming use letters(a-z), underscore, numbers(0-9)
# + is the concatination operation in python
_x = 5
y = "Automation"
print(_x)
print(y)

print("Hello "+ y)

x = 10
y = 25
print(x+y)

#Syntax
if 10 > 5:
    print("10 is greater than 5")

#Function
# use def then function name to create a function
def sum(a,b):
    print(a*b)
x = sum(10,20)

#CommandLine
# use the commanline or terminal to run the file

#Comments
# use # for single line comments
# to convert existing code into comment just select it press ctrl and forward slash
# to un comment just ctrl and forward slash

#Numbers
x = 5
y = 2.5
z = 4j
print(type(x))
print(type(y))
print(type(z))

a = int(2)     # 2
b = int(3.6)   # 3
c = float(5)   # 5.0
d = str(6)     # "6"

print(a)
print(b)
print(c)
print(d)

#Strings
x = "Hello World..."
y = "    Hello code  " # we use strip to trim the spaces at start and at end
z = "Hey, Guys"
print(x)
print(x[1])
print(x[6:11])
print(len(x))
print(x.lower())
print(x.upper())
print(y)
print(y.strip())
print(y.replace("e","a"))
print(z.split(","))

#Input
print("Please enter your name: ")
x = input()
print("Hello, "+x)

