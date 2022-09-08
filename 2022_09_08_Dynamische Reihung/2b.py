from abi2024 import *

def GetMinimum(array: DynArray):
    if array.isEmpty():
        return 0
    lowest = array.getItem(0)
    for index in range(1, array.getLength()):
        if array.getItem(index) < lowest:
            lowest = array.getItem(index)
    return lowest

alter = DynArray()
alter.append(21)
alter.append(20)
alter.append(33)
alter.append(30)
alter.append(27)
alter.append(28)
alter.append(31)
alter.append(19)

print(GetMinimum(alter))