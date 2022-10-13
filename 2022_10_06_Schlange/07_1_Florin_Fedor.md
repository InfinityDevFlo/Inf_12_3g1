# Aufgaben Schlange

## Aufgabe 1

```python

schlange = Queue()  # Schlange wird instanziert
if not schlange.isEmpty():  # Es wird überprüft, ob die Schlange leer ist
    print("Hallo Welt")  # Wenn die Schlange leer ist wird "Hallo Welt" ausgegeben
schlange.enqueue(5)  # 5 wird zur Schlange hinzugefügt
schlange.enqueue(1)  # 1 wird zur Schlange hinzugefügt
schlange.enqueue(4)  # 4 wird zur Schlange hinzugefügt
print(schlange.head())  # Das erste Element der Schlange wird ausgegeben, bleibt aber in der Schlange: 5 
print(schlange.dequeue())  # Das erste Element der Schlange wird ausgegeben, wird aber entfernt: 5
schlange.dequeue(2)  # Die Methode erlaubt keine Parameter. Entsprechend wird keine Methode gefunden die dem Aufruf entspricht

```