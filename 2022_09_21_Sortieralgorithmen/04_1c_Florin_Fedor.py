from abi2024 import *


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


def changePos(firstIndex: int, secondIndex: int, array: DynArray):
    first = array.getItem(firstIndex)
    second = array.getItem(secondIndex)
    array.setItem(firstIndex, second)
    array.setItem(secondIndex, first)


alter = DynArray()
alter.append(21)
alter.append(20)
alter.append(33)
alter.append(30)
alter.append(27)
alter.append(28)
alter.append(31)
alter.append(19)

print(selectionsort(alter).elements)
