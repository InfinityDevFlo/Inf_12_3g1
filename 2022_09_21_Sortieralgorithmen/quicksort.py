from abi2024 import *

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

alter = DynArray()

alter.append(21)
alter.append(20)
alter.append(33)
alter.append(30)
alter.append(27)
alter.append(28)
alter.append(31)
alter.append(19)

print(quicksort(alter).elements)
