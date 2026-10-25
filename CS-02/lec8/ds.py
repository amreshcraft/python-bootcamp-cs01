# CRUD  + methods 
l = [1,325,7632]

#  Create
l3 = list() 
l2 = []
# Update - append -insert -- allocate the memory
# l3[0] = 67 -- error
# l3[1] = 78  -- error
l3.append(67)
l3.append(78)

print(l3[0])
print(l3[1])

l3[0] = 98   # update only already exit indexed element
l3[1] = 456
# Read
print(l3[0])
print(l3[1])

t = (122,4,21)
d = {
    "name":"Amresh",
    "age":99
}

s = "Hey "

l.append