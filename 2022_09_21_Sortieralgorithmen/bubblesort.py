from abi2024 import *

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