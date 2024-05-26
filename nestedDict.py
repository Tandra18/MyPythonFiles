# myStudents = {
#     "student1" : {
#         "name" : "satt pi",
#         "age" : 24
#     },
#     "student2" : {
#         "name" : "minn khant",
#         "age" : 25
#     },
#     "student3" : {
#         "name" : "kaung min",
#         "age"  : "24"
#     }
#
# }
# print(myStudents)

stu1 = {
        "name" : "satt pi",
        "age" : "24"
    }
stu2 = {
        "name" : "minn khant",
        "age" : "25"
    }
stu3 = {
        "name" : "kaung min",
        "age"  : "24"
    }

myStudents = {
    "student1" : stu1,
    "student2" : stu2,
    "student3" : stu3
}
# print(myStudents)
# print(myStudents["student1"]["name"])

for x, obj in myStudents.items():
    print(x)

    for y in obj:
        print(y + ":" + obj[y])