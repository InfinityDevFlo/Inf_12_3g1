# 02_Wiederholung

## Aufgabe 1

```python
""" Funktionsdefinition """


def alter(jahr1, jahr2):
    return jahr2 - jahr1


aktuellesJahr = 2022
geburtsJahr = 2004

print(alter(geburtsJahr, aktuellesJahr))
```

- jahr1 (Wert: 2004, Typ: Integer), jahr 2 (Wert: 2022, Typ: Integer)-> Formaler Parameter
- aktuellesJahr (Wert: 2004, Typ: Integer), geburtsJahr (Wert: 2022, Typ: Integer) -> Aktueller Parameter
- alter(geburtsJahr , aktuellesJahr) -> Funktionsaufruf
- alter -> Funktionsname
- def alter(jahr1, jahr2): -> Funktionsdefinition
- jahr2 - jahr1 -> Rückgabeparameter (Wert: 18, Typ: Integer)

## Aufgabe 2

Die Erste Methode benötigt durch den Aufruf in einer Print anweisung zwangsläufig einen Rückgabewert, wohingegen, die
zweite Methode keinen braucht und sich eigentständing um eine Ausgabe kümmern muss.

## Aufgabe 3

a: TypeError: 'int' object is not iterable -> Falscher Datentyp
b: TypeError: unsupported operand type(s) for +=: 'int' and 'str' -> Falscher Datentyp
c: TypeError: unsupported operand type(s) for +=: 'int' and 'str' -> Falscher Datentyp

Zu b und c: Mit Strings kann nicht gerechnet werden. Bei b ist eine Liste vorhanden, da eine String eine Zeichenkette ist
+
