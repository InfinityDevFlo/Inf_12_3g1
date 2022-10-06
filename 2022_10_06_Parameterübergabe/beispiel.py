from abi2024 import *
from methods import *

def bsp_1(a):
    a = a ^ 2
    print(a)


def bsp_2(b):
    b = DynArray()
    b.append("Hallo")
    getDynArray(b)


def bsp_3(c):
    c.delete(0)
    c.append(" Hallo ")
    getDynArray(c)


def bsp_4(d):
    c = d
    c.delete(0)
    c.append(" Hallo ")
    getDynArray(c)

a = 3
bsp_1(a)
print(a)

print("_________________________")

b = DynArray()
b.append("Hi")
bsp_2(b)
getDynArray(b)

print("_________________________")

c = DynArray()
c.append("Hi")
bsp_3(c)
getDynArray(c)

print("_________________________")

d = DynArray()
d.append("Hi")
bsp_4(d)
getDynArray(d)


g = DynArray()
bsp_3(g)
bsp_3(DynArray())
