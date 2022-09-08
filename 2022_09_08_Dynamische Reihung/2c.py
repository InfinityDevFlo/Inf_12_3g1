from abi2024 import *

def GetMaximum(array: DynArray):
    if array.isEmpty():
        return 0
    highest = array.getItem(0)
    for index in range(1, array.getLength()):
        if array.getItem(index) > highest:
            highest = array.getItem(index)
    return highest


alter = DynArray()
alter.append(21)
alter.append(20)
alter.append(33)
alter.append(30)
alter.append(27)
alter.append(28)
alter.append(31)
alter.append(19)

print(GetMaximum(alter))