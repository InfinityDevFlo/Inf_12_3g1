# Stapel

````python

stapel = Stack() # Stapel wird Initialisiert
if stapel.isEmpty(): # Es wird überprüft ob der Stapel Elemente enthält
    print("Der Stapel ist voll") # Wenn der Stapel leer ist, wird dies ausgegeben
stapel.push(5) # Die 5 wird auf den Stapel gelegt
stapel.push(1) # Die 1 wird auf den Stapel gelegt
stapel.push(4) # Die 4 wird auf den Stapel gelegt
print(stapel.top()) # Das oberste Element des Stapels wird ausgegeben: 4 bleibt aber 
print(stapel.pop()) # Das oberste Element des Stapels wird ausgegeben: 4 wird entfernt
stapel.push(2) # Die 2 wird auf den Stapel gelegt
````