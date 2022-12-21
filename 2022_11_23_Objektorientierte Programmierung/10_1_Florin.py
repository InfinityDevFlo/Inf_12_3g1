class Auto(object):  # Definition der Klasse Auto
    tankinhalt = 0  # Setzen der Klassenattribute
    kilometerstand = 0  # Setzen der Klassenattribute

    def __init__(self, kennzeichen, tankvolumen, verbrauch):  # Definition des Konstruktors
        self.tankvolumen = tankvolumen  # Setzen der Objektattribute
        self.verbrauch = verbrauch  # Setzen der Objektattribute
        self.kennzeichen = kennzeichen  # Setzen der Objektattribute

    def getTankinhalt(self):  # Definition der Methode getTankinhalt
        return self.tankinhalt  # Rückgabe des Tankinhalts

    def getKilometerstand(self):  # Definition der Methode getKilometerstand
        return self.kilometerstand  # Rückgabe des Kilometerstandes

    def setKilometerstand(self, kilometerstand):  # Definition der Methode setKilometerstand
        self.kilometerstand = kilometerstand  # Setzen des Kilometerstandes

    def getTankvolumen(self):  # Definition der Methode getTankvolumen
        return self.tankvolumen  # Rückgabe des Tankvolumens

    def getVerbrauch(self):  # Definition der Methode getVerbrauch
        return self.verbrauch  # Rückgabe des Verbrauchs

    def getKennzeichen(self):  # Definition der Methode getKennzeichen
        return self.kennzeichen  # Rückgabe des Kennzeichens

    def setKennzeichen(self, kennzeichen):  # Definition der Methode setKennzeichen
        self.kennzeichen = kennzeichen  # Setzen des Kennzeichens

    def tanken(self, menge):  # Definition der Methode tanken
        self.tankinhalt += menge  # Hinzufügen der Menge zum Tankinhalt

    def fahren(self, strecke):  # Definition der Methode fahren
        verbraucht = self.verbrauch * strecke / 100
        if verbraucht > self.tankinhalt:
            raise NotEnoughFuelException("Nicht genug tankinhalt")
        self.tankinhalt -= verbraucht  # Verringern des Tankinhalts um den Verbrauch * die Strecke / 100
        self.kilometerstand += strecke  # Hinzufügen der Strecke zum Kilometerstand


class NotEnoughFuelException(Exception):

    def __init__(self, msg):
        print(msg)

auto = Auto("AB-CD-123", 50, 5)
auto.tanken(50)
auto.fahren(1000000000)