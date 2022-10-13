from abi2024 import *
from methods import *

def getQueueMaximum(queue: Queue):
    temp = copyQueue(queue)
    maximum = temp.dequeue()
    while not temp.isEmpty():
        current = temp.dequeue()
        if current > maximum:
            maximum = current
    return maximum

def getAmountOfElement(queue: Queue, element: int) -> int:
    temp = copyQueue(queue)
    amount = 0
    while not temp.isEmpty():
        if temp.dequeue() == element:
            amount += 1
    return amount

def removeAll(queue: Queue, element: int):
    temp = copyQueue(queue)
    temp2 = Queue()
    while not temp.isEmpty():
        first = temp.dequeue()
        if first != element:
            temp2.enqueue(first)

    return temp2

def sortQueue(queue: Queue) -> Queue:
    temp = copyQueue(queue)
    temp2 = Queue()
    while not getQueueSize(temp2) == getQueueSize(queue):
        maximum = getQueueMaximum(temp)
        amount = getAmountOfElement(temp, maximum)
        for i in range(amount):
            temp2.enqueue(maximum)
        temp = removeAll(temp, maximum)
    return temp2



noten = Queue()
noten.enqueue(5)
noten.enqueue(1)
noten.enqueue(10)
noten.enqueue(2)
noten.enqueue(10)
noten.enqueue(12)


getQueue(sortQueue(noten))
