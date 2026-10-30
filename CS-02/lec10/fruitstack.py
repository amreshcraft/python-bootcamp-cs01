FruitStack = []


def push_fruit(Fruit):
    if(Fruit["Price"] < 100):
        FruitStack.append(Fruit)
    else:
        print("Bahut mehga hai ...")
    

def pop_fruit():
    if(len(FruitStack) == 0):
        print("UNDERFLOW")
    else:
        FruitStack.pop()

