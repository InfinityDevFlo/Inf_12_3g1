class DynArray:
    def __init__(self):#erstellt leeres Array
        self.elements = []
    def isEmpty(self):#prüft, ob Array leer ist
        if self.elements == []:
            return True
        else:
            return False      
    def getItem(self,index):#gibt Element mit dem Index aus
        return self.elements[index]      
    def append(self,value):#fügt Element am Ende an
        self.elements.append(value)       
    def insertAt(self,index,value):#fügt Element an der Stelle ein
        self.elements.insert(index,value)       
    def setItem(self,index,value):#setzt den Wert des Elements mit dem Index
        self.elements[index] = value      
    def delete(self,index):#löscht ein Element mit bestimmten Index
        self.elements.pop(index)       
    def getLength(self):#Gibt die Anzahl an Elementen aus
        return len(self.elements)