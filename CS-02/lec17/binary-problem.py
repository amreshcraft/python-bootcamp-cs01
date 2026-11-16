import pickle as p

def Create():
    PNR = int(input("Enter your PNR number: "))
    PName = input("Enter your name: ")
    BRDSTN = input("Enter your boarding location: ")
    DESTN = input("Enter your destination: ")
    FARE = float(input("Enter your fare price: "))
    with open("PASSENGERS.DAT", "+ab") as f :
        
        data  = [PNR,PName,BRDSTN,DESTN,FARE]
        p.dump(data, f)
        print(f"data created successfully")



def Search_Destn(D):
    with open("PASSENGERS.DAT", "rb") as f :
        try : 
            while True :
               data = p.load(f)
               if(data[3] == D):
                  print(data)
        except EOFError as e :
            print("End of data ")
            
    print(f"data fetched successfully")



def UpdateFare():
    container = []
    with open("PASSENGERS.DAT", "rb") as f :
            try : 
                while True :
                   data = p.load(f)
                   if(data):
                        currentPrice = data[4] 
                        increasePrice = currentPrice + ( (5/100) * currentPrice)
                        data[4] = increasePrice
                        container.append(data)  
                       
            except EOFError as e :
                     pass
            except Exception as e :
                print("Something went wrong : ",e)
    
    with open("PASSENGERS.DAT","wb") as f2:
        for c in container :
             p.dump(c,f2)
                
    print(f"data updated successfully")






def Delete(PNR):
    container = []
    with open("PASSENGERS.DAT", "rb") as f :
            try : 
                while True :
                   data = p.load(f)
                   if(data):
                         if(data[0] != PNR) :
                           container.append(data)  
                       
            except EOFError as e :
                     pass
            except Exception as e :
                print("Something went wrong : ",e)
    
    with open("PASSENGERS.DAT","wb") as f2:
        for c in container :
             p.dump(c,f2)
                
    print(f"data deleted successfully")




def Copy_New():
    container = []
    with open("PASSENGERS.DAT", "rb") as f :
            try : 
                while True :
                   data = p.load(f)
                   if(data):
                      container.append(data)  
                       
            except EOFError as e :
                     pass
            except Exception as e :
                print("Something went wrong : ",e)
    
    with open("NewCopy.DAT","+ab") as f2:
        for c in container :
             p.dump(c,f2)
                
    print(f"data updated successfully")
    
    
    


def Display():
    with open("PASSENGERS.DAT", "rb") as f :
        try : 
            while True :
               data = p.load(f)
               print(data)
        except EOFError as e :
            print("End of data ")
            
    print(f"data fetched successfully")






# Create()
# Create()
# Create()
# Search_Destn("Mumbai")

# UpdateFare()
# Display()

Copy_New()