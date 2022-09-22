"""

Implementation aller Klassen und Methoden gemäß der Bestimmungen für das Abitur Informatik 2024

https://www.nibis.de/uploads/mk-bolhoefer/2024/18InformatikHinweise2024.pdf

"""


class DynArray:
    """
    Die Dynamische Reihung ist eine List von Elementen, die es ermöglicht mittels Index diese Liste beliebig zu bearbeiten
    """

    def __init__(self):
        """
        Initialisierung -> Leeres Array wird erstellt
        """
        self.elements = []

    def isEmpty(self) -> bool:
        """
        Überprüfung ob das Array Elemente beinhaltet. Entsprechend wird beim Leeren Array True zurückgegeben
        Sobald das Array mindestens einen Wert erhält ist der Rückgabewert False
        
        :return: Wenn das Array Leer ist True. Ansonsten False
        """
        return self.elements == []

    def getItem(self, index):
        """
        
        
        :param index: Der Index des benötigten Elements
        :return: Den Wert der sich hinter dem Index verbirgt, solange er verfügbar ist. Anderenfalls wird ein Indexerror ausgegeben
        """
        return self.elements[index]

    def append(self, value):
        """
        Fügt einen Wert zum Array hinzu
        
        :param value: Der Wert der hinzugefügt werden soll 
        :return: 
        """
        self.elements.append(value)

    def insertAt(self, index, value):
        """
        Fügt <value> an der stelle <index> ein und erhöht den Index aller folgenden Elemente um 1
        """
        self.elements.insert(index, value)

    def setItem(self, index, value):
        """
        Der Index: <index> wird mit dem Wert <value> überschrieben
        """
        self.elements[index] = value

    def delete(self, index):
        """
        Löscht einen Wert an einem bestimmten Index
        
        :param index: Index des zu löschenden Elements
        :return: 
        """
        self.elements.pop(index)

    def getLength(self) -> int:
        """
        Gibt die Anzahl aller Elemente des Arrays zurück
        """
        return len(self.elements)


class Stack:
    """
    Der Stack (Stapel) arbeitet nach dem Last in - First Out Prinzip. Entsprechend werden die Elemente "aufeinandergelegt
    """

    def __init__(self):
        """
        Initialisierung des Stapels
        """
        self.elements = []

    def isEmpty(self) -> bool:
        """
        Überprüfung ob der Stapel Elemente beinhaltet. Entsprechend wird beim Leeren Stapel True zurückgegeben
        sobald der Stapel mindestens einen Wert erhält ist der Rückgabewert False

        :return: Wenn der Stapel Leer ist True. Ansonsten False
        """
        return self.elements == []

    def top(self):
        """
        Gibt das oberste Element des Stapels zurück, behält es aber auf dem Stapel
        """
        return self.elements[len(self.elements) - 1]

    def push(self, value):
        """
        Legt einen Wert auf den Stapel
        
        :param value: Wert der auf den Stapel gelegt wird
        :return: 
        """
        self.elements.append(value)

    def pop(self):
        """
        Gibt das oberste Element des Stapels zurück und entfernt es dabei vom Stapel
        """
        return self.elements.pop()


class Queue:
    """
    Die Queue (Schlange) arbeitet nach dem First in - First Out Prinzip. 
    Dabei ist es aufgebaut wie eine Warteschlange und lässt das erste Element auch zuerst raus
    """

    def __init__(self):
        """
        Initialisierung der Queue
        """
        self.elements = []

    def isEmpty(self) -> bool:
        """
        Überprüfung ob die Queue Elemente beinhaltet. Entsprechend wird beim Leeren Array True zurückgegeben
        Sobald die Queue mindestens einen Wert erhält ist der Rückgabewert False

        :return: Wenn die Queue Leer ist True. Ansonsten False
        """
        return self.elements == []

    def head(self):
        """
        Gibt das erste Element der Queue zurück. Das Element bleibt jedoch weiterhin in der Queue enthalten

        :return: Das erste Element. Sofern die Liste Leer ist erscheint ein IndexError
        """
        return self.elements[0]

    def enqueue(self, value):
        """
        Fügt einen Wert zur Queue hinzu

        :param value: Wert der an die Queue gehängt werden soll
        :return:
        """
        self.elements.append(value)

    def dequeue(self):
        """
        Gibt das vorderste Element der Queue zurück und entfernt dieses

        :return: Das erste Element. Sofern die Liste Leer ist erscheint ein IndexError
        """
        return self.elements.pop(0)


class BinTree:
    """
    Der BinTree (Binärbaum) ermöglicht es an einen Wurzel
    bzw. ein Element die entsprechend gesetzt werden kann,
    weitere Instanzen zu hängen und somit zu verschachteln
    """

    def __init__(self):
        """
        Initialisierung des Baums ohne Startwert
        """
        self.item = None
        self.right = None
        self.left = None

    def __init__(self, item):
        """
        Initialisiert den Baum mit dem entsprechenden Startwert
        :param item: Der Wert, dem die Wurzel des Baumes zu Beginn annimmt
        """
        self.item = item
        self.right = None
        self.left = None

    def hasItem(self):
        """
        Überprüft ob zurzeit eine Wurzel gesetzt wurde
        :return: True wenn das Item vorhanden ist. Anderenfalls False
        """
        return self.item is not None

    def getItem(self):
        """
        Gibt die aktuelle Wurzel zurück sofern dies vorhanden ist
        :return: Die aktuelle Wurzel
        """
        return self.item

    def setItem(self, item):
        """
        Setzt den Wert der Wurzel
        :param item: neuer Wert für die Wurzel
        :return:
        """
        self.item = item

    def deleteItem(self):
        """
        Löscht die aktuelle Wurzel
        :return:
        """
        self.item = None

    def isLeaf(self) -> bool:
        """
        Überprüft ob der Baum weitere Teilbäume (Links und/oder Rechts) besitzt
        :return: Ob der linke und Rechte Teilbaum **nicht** vorhanden sind
        """
        return self.left is None and self.right is None

    def hasLeft(self) -> bool:
        """
        Überprüft ob ein Linker Ast vorhanden ist
        :return: True wenn der Linke Ast nicht Null ist
        """
        return self.left is not None

    def getLeft(self) -> "BinTree":
        """
        Gibt den Linken Ast zurück sofern vorhanden
        :return:
        """
        return self.left

    def setLeft(self, value: "BinTree"):
        """
        Setze einen neuen Wert für den Linken Ast
        :param value: Der Wert der gesetzt werden soll
        :return:
        """
        self.left = value

    def deleteLeft(self):
        """
        Löscht den Wert des Linken Astes
        :return:
        """
        self.left = None

    def hasRight(self) -> bool:
        """
        Überprüft ob ein Rechter Ast vorhanden ist
        :return: True wenn der Rechte Ast nicht Null ist
        """
        return self.right is not None

    def getRight(self) -> "BinTree":
        """
        Gibt den Rechten Ast zurück sofern vorhanden
        :return:
        """
        return self.right

    def setRight(self, value: "BinTree"):
        """
        Setze einen neuen Wert für den Rechten Ast
        :param value: Der Wert der gesetzt werden soll
        :return:
        """
        self.right = value

    def deleteRight(self):
        """
        Löscht den Wert des Rechten Astes
        :return:
        """
        self.right = None
