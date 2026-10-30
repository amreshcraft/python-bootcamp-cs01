stack = []
capacity = 5

def createStack(cap):
    global capacity
    capacity = cap
    
    
def push(data):
    if(len(stack) == capacity):
        print("Stack is full")
        print("Failed to push data in stack!!!")
    else:   
        stack.append(data)

def isEmpty():
    return len(stack) == 0

def pop():
    stack.pop()

def peek():
    return stack[len(stack) - 1]

def display():
    print(stack)