thisdict =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year" : 1964,
}
x = thisdict["year"]
y = thisdict.get("model")
z = thisdict.keys()
w = thisdict.values()
a = thisdict.items()
# print(x)
# print(y)
# print(z)

thisdict["color"] = ("red", "blue", "white")
thisdict["eng power"] = "3.5cc"
# print(thisdict)
# print(z)
# print(w)

thisdict["year"] = 2014
print(a)
if "model" in thisdict:
    print("yes, car model is present")
else:
    print("car model does not present")

