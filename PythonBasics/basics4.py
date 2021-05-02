# in python every function has the self as the very first argument, we can also rename it
# in python every class has inbuilt function called __init__ and also we can explicitly define it
# while creating object for the class init is the function which is always called
class Myclass():
    name = 'Raghav'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)


x = Myclass('Rahul', 23)
print(x.name)
x.sum(10,20)
print(x.age)
del x.name    # it will delete the reference of the object
print(x.name)