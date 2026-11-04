# n = [10,20,30]
# print(n)
# n.append(40) 
# print(n) # [10,20,30,40]
# n.append([45,55,66]) 
# print(n) # [10,20,30,40,45,55,66] - error -- correct = [10,20,30,40,[45,55,66]]
# n.pop()
# print(n)

# n.insert(2,25) # (index, value)
# print(n) # [10,20,25,30,40]

# n.remove(20)
# print(n) # 

b = [ 4,56,342,5,23,43,2,31,1]
print(b)
b.sort()
print(b)

r = [5,63,2,3,1]
t = sorted(r)
print(r)
print(t)


p = [1,2,3,4,54,4,4,4,6,4,5]
s = p.count(4)
print(p) # [1,2,3,4,54,4,4,4,6,4,5]
print(s)

a1 = [ 1,2,3,4]
a2 = [5,6,7,8]
a3 = a1 + a2
print(a1) # same1
print(a2) #  same2
print(a3)  # same1+same2

a2.extend(a1)  # original list changes
print(a1)
print(a2)

a2.reverse()
print(a2)

v = a2.index(8)
print(v)



a2.clear()
print(a2)



list2 = [10,20,30]
list3 = list2
list3.append(40)
print(list2) # [10,20,30,40]


list4 = [10,20,30]
list5 = list4.copy()
list5.append(40)
print(list4) 