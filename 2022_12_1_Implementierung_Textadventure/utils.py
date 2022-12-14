import os
from abi2024 import *

PLAYERINSTANCE = None


def clearScreen():
    print("\x1B[2J")


def GetMinimum(array: DynArray):
    if array.isEmpty():
        return 0
    lowest = array.getItem(0)
    for index in range(1, array.getLength()):
        if array.getItem(index) < lowest:
            lowest = array.getItem(index)
    return lowest


def GetMaximum(array: DynArray):
    if array.isEmpty():
        return 0
    highest = array.getItem(0)
    for index in range(1, array.getLength()):
        if array.getItem(index) > highest:
            highest = array.getItem(index)
    return highest


def bubblesort(array: DynArray) -> DynArray:
    for index in range(array.getLength()):
        for index2 in range(array.getLength() - 1):
            if array.getItem(index2) > array.getItem(index2 + 1):
                changePos(index2, index2 + 1, array)
    return array


def changePos(index1: int, index2: int, array: DynArray):
    first = array.getItem(index1)
    second = array.getItem(index2)
    array.setItem(index1, second)
    array.setItem(index2, first)


def sublist(start: int, end: int, array: DynArray) -> DynArray:
    result = DynArray()
    for i in range(start, end):
        result.append(array.getItem(i))
    return result


def mergesort(array: DynArray) -> DynArray:
    if array.getLength() > 1:
        middle = array.getLength() // 2
        left = sublist(0, middle, array)
        right = sublist(middle, array.getLength(), array)
        mergesort(left)
        mergesort(right)

        l = r = k = 0

        while l < left.getLength() and r < right.getLength():
            if left.getItem(l) <= right.getItem(r):
                array.setItem(k, left.getItem(l))
                l += 1
            else:
                array.setItem(k, right.getItem(r))
                r += 1
            k += 1

        for index in range(l, left.getLength()):
            array.setItem(k, left.getItem(index))
            k += 1

        for index in range(r, right.getLength()):
            array.setItem(k, right.getItem(index))
            k += 1

    return array


def sortStack(stack: Stack) -> Stack:
    sorted = Stack()
    while not stack.isEmpty():
        highest = stack.pop()
        while not sorted.isEmpty() and sorted.top() < highest:
            stack.push(sorted.pop())
        sorted.push(highest)
    return sorted


def quicksort(array: DynArray) -> DynArray:
    if array.getLength() > 1:
        pivot = array.getItem(array.getLength() // 2)
        left = DynArray()
        right = DynArray()

        # Teilen in Linke und rechte liste
        for index in range(array.getLength()):
            if array.getItem(index) < pivot:
                left.append(array.getItem(index))
            elif array.getItem(index) > pivot:
                right.append(array.getItem(index))

        # rekursiver aufruf der methode für die linke und rechte hälfte
        quicksort(left)
        quicksort(right)

        # Clear des Arrays
        for index in range(array.getLength()):
            array.delete(0)

        # Einfügen der Elemente
        for index in range(left.getLength()):
            array.append(left.getItem(index))
        array.append(pivot)
        for index in range(right.getLength()):
            array.append(right.getItem(index))
    return array


def selectionsort(array: DynArray) -> DynArray:
    sorted = DynArray()
    for index in range(array.getLength()):
        lowestPosition = findLowestPosition(array)
        lowestItem = array.getItem(lowestPosition)
        array.delete(lowestPosition)
        sorted.append(lowestItem)

    return sorted


def findLowestPosition(array: DynArray) -> int:
    min = 0
    for index in range(array.getLength()):
        if array.getItem(min) > array.getItem(index):
            min = index
    return min


def copyQueue(queue: Queue):
    temp = Queue()
    temp2 = Queue()
    while not queue.isEmpty():
        temp.enqueue(queue.head())
        temp2.enqueue(queue.dequeue())
    while not temp.isEmpty():
        queue.enqueue(temp.dequeue())
    return temp2


def getQueueSize(queue: Queue) -> int:
    temp = copyQueue(queue)
    size = 0
    while not temp.isEmpty():
        size += 1
        temp.dequeue()
    return size


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


class Map(object):

    def __init__(self):
        self.keys = DynArray()
        self.values = DynArray()

    def get(self, key: str):
        index = None
        for i in range(self.keys.getLength()):
            if self.keys.getItem(i) == key:
                index = i
        if index is not None:
            return self.values.getItem(index)
        else:
            return None

    def put(self, key: str, value: object):
        index = None
        for i in range(self.keys.getLength()):
            if self.keys.getItem(i) == key:
                index = i
        if index is not None:
            self.values.setItem(index, value)
        else:
            self.keys.append(key)
            self.values.append(value)

    def remove(self, key: str):
        index = None
        for i in range(self.keys.getLength()):
            if self.keys.getItem(i) == key:
                index = i
        if index is not None:
            self.keys.delete(index)
            self.values.delete(index)

    def containsKey(self, key: str) -> bool:
        for i in range(self.keys.getLength()):
            if self.keys.getItem(i) == key:
                return True
        return False

    def containsValue(self, value: object) -> bool:
        for i in range(self.values.getLength()):
            if self.values.getItem(i) == value:
                return True
        return False

    def isEmpty(self) -> bool:
        return self.keys.getLength() == 0

    def size(self) -> int:
        return self.keys.getLength()

    def clear(self):
        self.keys = DynArray()
        self.values = DynArray()

    def keySet(self) -> DynArray:
        return self.keys

    def values(self) -> DynArray:
        return self.values


def arrayToSeparatedString(array: DynArray, separator: str = ", ") -> str:
    string = ""
    for i in range(array.getLength()):
        string += str(array.getItem(i))
        if i != array.getLength() - 1:
            string += separator
    return string