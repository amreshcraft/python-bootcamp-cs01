

n = "Yuvraj"

# print(n)
# print(n[:])
# print(n[0:])
# print(n[:6])
# print(n[::2])
# print(n[::-2])
print("size: ",len(n))
print(n[::-1])
print(n[-1:-7:-1]) # jarvuY
print(n[-1: -(len(n) + 1):-1]) 
print(n[:2:-1])  # jar 
print(n[:-2:-1]) # Yuvraj ---> jarvuY ---> -2==a ---> j
print(n[:-1:-1]) # s = -1 , end = -1, reverse = -1 ,Yuvraj-> jarvuY--> empty 
print(n[:-1:-2]) # s = -1 , end = -1 , Yuvraj --> empty
print(n[:-1:2]) # s = 0 , end = -1 == 5 , step = 2 , print-> 0 + 2 + 4 
