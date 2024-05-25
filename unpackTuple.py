# fruits = ("apple", "banana","orange")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# using asterisk
fruits = ("apple", "banana","orange", "strawberry","coconut")
# (green, yellow, *red) = fruits
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)