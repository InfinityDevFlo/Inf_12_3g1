# Arbeitsblatt Python Wiederholung

## Aufgabe 1

- print (3+5)
  -> Die Ziffern werden zum Ergebnis 8 Addiert und durch die Anweisung "print" ausgegeben
  <br><br>
- print (3+5.0)  -> Die Ganze Zahl 3 (Integer) wird mit der Gleitkommazahl 5,0 (Float) addiert, sodass man als ausgabe
  8.0 erhält. Da Integer + Float = Float (Sofern das ganze für einen Float von der Größe her ausreicht)
  <br><br>
- print (3*5) ->
  Der Operator "\*" multipliziert. Da beides Integer sind erhält man als Ergebnis ebenfalls einen Integer: 8
  <br><br>
- print (3**3) ->
  Durch die Operation "\*\*" wird die Potenz der beiden Zahlen ausgerechnet. Entsprechend ergibt 3 (Basis) hoch 3 (
  Exponent) dann 27
  <br><br>
- print (5%3) -> Der Operator % bildet das modulo der Zahlen (modulo = Rest der Division). Entsprechend ist die Ausgabe
  2, Da 3 genau 1 Mal ganz in die 5 passt und dort dann ein Rest von 2 bleibt
  <br><br>
- print (9/3) -> Der Operator "/" führt eine Division aus und gibt dabei das Ergebnis als Float zurück. Entsprechend
  wird hier 3.0 ausgegeben
  <br><br>
- print ( '3 '+ '3 ') -> Die 3 ist hier nicht als Zahl, sondern als Text angegeben. Entsprechend werden hier dann die
  beiden Texte aneinandergereiht. Somit ergibt sich die Ausgabe: 3 3
  <br><br>
- print (10//3) -> Durch das doppelte // wird restlos dividiert. Somit ergibt sich als Ergebnis immer eine Ganze Zahl (
  Integer). Die Ausgabe ist hier somit 3, da die 3 nur 3 mal ganz in die 10 passt. der Rest wird hier Ignoriert

## Aufgabe 2

Bei x=y wird der Variable x der Wert von y zugewiesen. Bei y=x geschieht das ganze umgekehrt. Hier wird der Variable y
der Wert der Variable x zugewiesen.

## Aufgabe 3

Da das gegebene Alter mit 70 Jahren über dem Seniorenalter liegt (senior_from_age) wird der Preis in der If Abfrage
entsprechend auf 2,5 gesetzt, da Senioren hier auch den adult_ticket Preis zahlen. Somit ergibt sich folgende Ausgabe:
Somebody who is 70 years old will pay 2.5 to ride the bus .

## Aufgabe 5

1. altitude < 1000 and speed > 100 -> False da altitude 1000 ist und nicht darüber
2. (propulsion== "Jet" or propulsion == "Turboprop") and speed < 300 or altitude < 20000 -> True, da propilsion weder
   Jet noch Turboprop ist. Da dannach jedoch eine Abfrage mit "or" durchgeführt wird, welche Wahr ist, ergibt sich das
   gesamtergebnis True
3. not (speed > 400 and propulsion == "Propeller") -> True, da speed > 400 False ist. Somit ist die gesamte Klammer
   False. Dadurch das das Ergebnis mit dem keyword "not" invertiert wird, ergibt sich das ergebnis True


