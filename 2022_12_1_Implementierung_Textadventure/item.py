class Item(object):

    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    def getId(self) -> str:
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description


class Key(Item):

    def __init__(self):
        super().__init__("key", "Schlüssel", "Wird zum öffnen des Fahrstuhls im Erdgeschoss benötigt")
