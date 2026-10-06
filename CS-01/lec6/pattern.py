# for i in range(1, 6):
#     for j in range(1, 6):
#         if(j <= i):
#            print(j,end=" ")
#         else:
#             print(end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(1,i+1):
#         print(j,end=" ")   
#     print()





# baharWala = 1 
# while baharWala <= 5:
#     andarWala = 1
#     while andarWala <= baharWala :
#         print(andarWala,end=" ")
#         andarWala  = andarWala + 1
#     print()
#     baharWala = baharWala + 1


#  #   #  #
#         #    
#         #   
#  #   #  # 


for t in range(4):
    for k in range (4):
        if( t == 0 or t == 3 ):
            print("#",end="  ")
        elif(k == 0 or k == 3): 
         	print("#",end="  ")
        else:
            print(end="   ")
    print()  