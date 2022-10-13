from abi2024 import *
from methods import *

# 2a

def getQueue(queue: Queue):
    temp = Queue()
    while not queue.isEmpty():
        print(queue.head())
        temp.enqueue(queue.dequeue())
    while not temp.isEmpty():
        queue.enqueue(temp.dequeue())


# 2b

def getMostCommonElement(queue: Queue):
    temp = copyQueue(queue)
    mostCommonElement = None
    mostCommonElementCount = 0
    while not temp.isEmpty():
        currentElement = temp.dequeue()
        currentElementCount = 1
        while currentElement in temp.elements:
            currentElementCount += 1
            temp.dequeue()
        if currentElementCount > mostCommonElementCount:
            mostCommonElement = currentElement
            mostCommonElementCount = currentElementCount
    return mostCommonElement, mostCommonElementCount


# 2c

def flipQueue(queue: Queue):
    temp = copyQueue(queue)
    temp2 = Queue()
    while not temp.isEmpty():
        for i in range(getQueueSize(temp) - 1):
            temp.enqueue(temp.dequeue())
        temp2.enqueue(temp.dequeue())
    return temp2




noten = Queue()
noten.enqueue(9)
noten.enqueue(7)
noten.enqueue(10)
noten.enqueue(10)
noten.enqueue(12)

getQueue(noten)

print("_________________________")

print(getMostCommonElement(noten))

print("_________________________")

getQueue(flipQueue(noten))