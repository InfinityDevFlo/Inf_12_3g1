def min(list) -> int:
    size = len(list)
    if size == 0:
        return 0
    if size == 1:
        return list[0]
    lowest = list[0]
    for i in list[1:]:
        if i < lowest:
            lowest = i
    return lowest

print(min([0, 6, 1, 10, -6]))

