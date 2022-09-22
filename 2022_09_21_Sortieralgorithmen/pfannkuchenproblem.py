from abi2024 import *

def sort(stack: Stack) -> Stack:
    sorted = Stack()
    while not stack.isEmpty():
        highest = stack.pop()
        while not sorted.isEmpty() and sorted.top() < highest:
            stack.push(sorted.pop())
        sorted.push(highest)
    return sorted


alter = Stack()

alter.push(21)
alter.push(20)
alter.push(33)
alter.push(30)
alter.push(27)
alter.push(28)
alter.push(31)
alter.push(19)

alter = sort(alter)

while not alter.isEmpty():
    print(alter.pop())
