# d1 = {
#     "name":"Amresh",
#     "age":26,
#     "highestQualification":"MCA",
#     "color":"Black"
# }

# # creating using constructor/method/function
# d2 = dict({"name":"Amresh"})
# print(d2)
# # read
# print(d1["highestQualification"])

# #update
# d1["age"] = 99

# print(d1)

# # delete
# del d1["color"]
# print(d1)


d3 = {
    "name" :"Riya",
    "age" : 15,
    "class":12,
    "stream":"maths"
}

print(d3)
# d3.clear() # empty the dictionary
# print(d3)
k = d3.keys()  # see like list but not list
print(k)
l2 = list(k)
print(l2)
# v = d3.values()
# print(v)

i = d3.items()
print(i)
il = list(i)
print(il)

for i in d3.items() :
    print(i[1])

dlist = list(d3.items())
print(dlist[2][1])

d3.pop()
