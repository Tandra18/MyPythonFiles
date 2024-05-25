# fruits = ["apple","strawberry","orange","lemon","onion","pineapple"]
# newlist =[]
#
# for x in fruits:
#     if "o" in x:
#         newlist.append(x)
#
#
# print(newlist)

#newlist = [expression for item in iterable if condition == True]


fruits = ["apple","strawberry","orange","lemon","onion","pineapple"]
# newlist = [x for x in fruits]
# newlist =[x for x in fruits if "a" in x]
# newlist = [ x for x in fruits if x!="apple"]
# newlist = [x for x in range(10)]
# newlist = [x for x in range(10) if x<3]
# newlist = [x.upper() for x in fruits]
# new = [x.upper() for x in newlist]
# newlist = ['hello' for x in fruits]
newlist = [x if x!="apple" else "orange" for x in fruits]

print(newlist)


