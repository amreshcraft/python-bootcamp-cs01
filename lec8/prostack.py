Container = [] # ye not accessible h so user dont apply any list method

# SIZE = 0
CAPACITY = 10

def createProStackWithCapacity(size):
   global CAPACITY 
   CAPACITY = size

def push(data):
    global  CAPACITY
    if(len(Container) <= CAPACITY -1 ):
        Container.append(data)
        # SIZE = SIZE + 1
    else :
        print("Overflow : stack is full")


def pop():
    if(isEmpty()):
        print("Nothing is left to pop ")
    else:
        # global SIZE
        Container.pop()
        # SIZE = SIZE - 1 

def peek():
    return Container[len(Container) - 1]

def isEmpty():
    return len(Container) == 0

def size():
    return len(Container)

def display():
    for v in Container:
        print(v,end="  , ")
    print("\nEnd")