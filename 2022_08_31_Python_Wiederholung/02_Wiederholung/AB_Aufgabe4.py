import math


def quader(a: int, b: int, c: int) -> int:
    return 2 * a * b + 2 * a * c + 2 * b * c


def zylinder(h: int, r: int) -> int:
    G = math.pi * (r ** 2)
    U = 2 * math.pi * r
    M = U * h
    return M + 2 * G
