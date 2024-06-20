# def myFunc():
#     x = 300
#     def myInnerFunc():
#         print(x)
#     myInnerFunc()
#
# myFunc()

x = 300

# def myFunc():
#     x = 250
#     print(x)
# myFunc()
#
# print(x)

# x = 300
# def myFunc():
#     global x
#     x =230
# myFunc()
# print(x)

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 