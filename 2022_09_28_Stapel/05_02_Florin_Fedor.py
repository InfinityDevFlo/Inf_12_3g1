from abi2024 import *

def flip(stack: Stack) -> Stack:
    flipped = Stack()
    while not stack.isEmpty():
        flipped.push(stack.pop())
    return flipped

def getStack(stack: Stack) -> Stack:
    printed = Stack()
    while not stack.isEmpty():
        element = stack.pop()
        printed.push(element)
        print(element)
    return flip(printed)

def stackGetMinimum(stack: Stack):
    lowest = stack.pop()
    while not stack.isEmpty():
        element = stack.pop()
        if element < lowest:
            lowest = element
    print(lowest)

def stackGetMaximum(stack: Stack):
    highest = stack.pop()
    while not stack.isEmpty():
        element = stack.pop()
        if element > highest:
            highest = element
    print(highest)


noten = Stack()
noten.push(9)
noten.push(7)
noten.push(10)
noten.push(12)

getStack(noten)

print("_______")

noten.push(9)
noten.push(7)
noten.push(10)
noten.push(12)

getStack(flip(noten))

print("_______")

noten.push(9)
noten.push(7)
noten.push(10)
noten.push(12)

stackGetMinimum(flip(noten))

print("_______")


noten.push(9)
noten.push(7)
noten.push(10)
noten.push(12)

stackGetMaximum(flip(noten))


print("_______")
noten.push(9)
noten.push(7)
noten.push(10)
noten.push(12)

getStack(noten)