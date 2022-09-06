# 02_Wiederholung

## Aufgabe 1

### a)

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

### b)

Die Methode "alter" löst das Problem zum Errechnen des Alters durch die Differenz des Aktuellen Jahres und des
Geburtsjahres.
Es ist somit ein Algorithmus vorhanden, da ein Problem hier durch fest definierte Handlungsanweisungen gelöst wird.

## Aufgabe 2

Die Erste Methode benötigt durch den Aufruf in einer Print anweisung zwangsläufig einen Rückgabewert, wohingegen, die
zweite Methode keinen braucht und sich eigentständing um eine Ausgabe kümmern muss.

## Aufgabe 3

a: TypeError: 'int' object is not iterable -> Falscher Datentyp<br>
b: TypeError: unsupported operand type(s) for +=: 'int' and 'str' -> Falscher Datentyp<br>
c: TypeError: unsupported operand type(s) for +=: 'int' and 'str' -> Falscher Datentyp

Zu b und c: Mit Strings kann nicht gerechnet werden. Bei b ist eine Liste vorhanden, da eine String eine Zeichenkette
ist

## Aufgabe 5

```python

def zylinder_volumen(hoehe, radius):
    pi = 3.14
    volumen = hoehe * pi * radius ** 2


zylinder_volumen(10, 3)
print(volumen)
# volumen ist in der Methode definiert. 
# Entsprechend kann hier nicht drauf zugegriffen werden
# Außerdem gibt die methode weder was zurück noch wird was ausgegeben
```

korrigiert:

```python
def zylinder_volumen(hoehe, radius):
    pi = 3.14
    volumen = hoehe * pi * radius ** 2
    return volumen


volumen = zylinder_volumen(10, 3)
print(volumen) 
```