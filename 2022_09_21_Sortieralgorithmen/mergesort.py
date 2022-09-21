from abi2024 import *


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


alter = DynArray()

alter.append(21)
alter.append(20)
alter.append(33)
alter.append(30)
alter.append(27)
alter.append(28)
alter.append(31)
alter.append(19)

print(mergesort(alter).elements)
