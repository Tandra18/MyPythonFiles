# class myClass:
#     x = 5
# p1 = myClass()
# print(p1.x)

# class myClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = myClass("Naung", 24)
# print(p1.name)
# print(p1.age)


# class myClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}[{self.age}]"
# p1 = myClass("naung",24)
# print(p1)


# class Person:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def __str__(self):
#         return f"'Hello my name is '{self.name} and [{self.age}] years old, and my height is ({self.height})"
# p1 = Person("Naung",24,"5foot 7inches")
# print(p1)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
# p1 = Person("naung",24)
# p1.myfunc()


class Person:
    def __init__(myobj, name, age):
        myobj.name = name
        myobj.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name + f"and [{abc.age}] years old")
p1 = Person("naung ",24)
p1.myfunc()
p1.age = 40
p1.myfunc()


