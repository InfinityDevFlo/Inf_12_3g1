from abi2024 import *


def GetDynArryay(array: DynArray):
    for index in range(array.getLength()):
        print(array.getItem(index))


alter = DynArray()
alter.append(21)
alter.append(20)
alter.append(33)
alter.append(30)
alter.append(27)
alter.append(28)
alter.append(31)
alter.append(19)
GetDynArryay(alter)


