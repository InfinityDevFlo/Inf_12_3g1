from abi2024 import *


def getDynArray(array: DynArray):
    for i in range(array.getLength()):
        print(array.getItem(i))


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


def sortQueue(queue: Queue) -> Queue:
    sorted = Queue()
    while not queue.isEmpty():
        highest = queue.dequeue()
        while not sorted.isEmpty() and sorted.head() < highest:
            queue.enqueue(sorted.dequeue())
        sorted.enqueue(highest)
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
