def arithMittel1(list):
    n = 0
    for i in list:
        n += i
    return n / len(list)


def arithMittel2(list):
    n = 0
    for i in list:
        n += i
    print(n / len(list))


notenliste = [10, 11, 12, 13, 14]  #
arithMittel2(notenliste)
print(arithMittel1(notenliste))
