## Python HA 2

## Aufgabe 1 (20 Punkte)
Schreibe ein Programm, das den Benutzer nach einer Ganzzahl fragt. Wenn die Zahl kleiner als Null ist, sollte das Programm die mit -1 multiplizierte Zahl ausgeben. Andernfalls gibt das Programm die Nummer unverändert aus. Bitte sehen Sie sich unten die Beispiele für erwartetes Verhalten an.

Beispielsausgabe:
```shell
Please type in a number: -7
The absolute value of this number is 7

Please type in a number: 1
The absolute value of this number is 1
```
### Aufgabe 2 (20 Punkte)

Öffne die Datei "ha2_aufgabe2_bugs.py" und behebe alle Fehler im Code.

### Aufgabe 3 (30 Punkte)
Schreibe ein Taschenrechner-Programm, das den Benutzer nach zwei Zahlen und einer Operation fragt. Wenn es sich bei der Operation um einer gültigen arithmetischen Operation handelt, sollte das Programm das Ergebnis der Operation mit den angegebenen Zahlen berechnen und ausdrucken. Wenn der Benutzer etwas anderes eingibt, sollte das Programm „Unbekannte Eingabe“ ausgeben.

Beispielsausgabe:
```shell
Number 1: 10
Number 2: 17
Operation: add

10 + 17 = 27
```
### Aufgabe 4 (30 Punkte)

1. Erstelle eine Liste von Zahlen von 1 bis 20. Welche Funktion kannst du dafür benutzen?
2. Bearbeite die Ausgangsliste mit einer For-Schleife, um eine neue Liste zu erstellen, die nur Zahlen enthält, die sowohl durch 2 als auch durch 3 teilbar sind.
3. Verwende jetzt eine List Comprehension, um eine neue Liste zu erstellen, die nur Zahlen enthält, die sowohl durch 2 als auch durch 3 teilbar sind.

## Extra Aufgaben für Extra Punkte

### Extra 1 (30 Punkte)

Schreibe ein Programm, das nach der Wettervorhersage für morgen fragt und dann wettergerechte Kleidung vorschlägt.

Der Vorschlag sollte sich ändern, wenn die Temperatur (gemessen in Grad Celsius) über 20, 10 oder 5 Grad liegt und auch wenn Regen auf dem Radar ist.

Beispielsausgabe:
```shell
What is the weather forecast for tomorrow?
Temperature: 21
Will it rain (yes/no): no
Wear jeans and a T-shirt

What is the weather forecast for tomorrow?
Temperature: 11
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well

What is the weather forecast for tomorrow?
Temperature: 7
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you

What is the weather forecast for tomorrow?
Temperature: 3
Will it rain (yes/no): yes
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order
Don't forget your umbrella!
```

### Extra 2 (40 Punkte)

Python-Vergleichsoperatoren können auch für Zeichenfolgen verwendet werden. String a ist kleiner als String b, wenn er alphabetisch vor b steht. Beachte jedoch, dass der Vergleich nur dann zuverlässig ist, wenn:
- die verglichenen Zeichen haben die gleiche Groß- und Kleinschreibung, d. h. beide GROSSBUCHSTABEN oder beide Kleinbuchstaben
- es wird nur das englische Standardalphabet von a bis z oder A bis Z verwendet.
Schreibe Sie ein Programm, das den Benutzer nach zwei Wörtern fragt. Das Programm sollte dann diejenige der beiden ausdrucken, die alphabetisch an letzter Stelle steht.
Du kannst davon ausgehen, dass alle Wörter vollständig in Kleinbuchstaben eingegeben werden.

Beispielsausgabe:
```shell
Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.

Please type in the 1st word: zorro
Please type in the 2nd word: batman
zorro comes alphabetically last.

Please type in the 1st word: python
Please type in the 2nd word: python
You gave the same word twice.
```

### Extra 3 (30 Punkte)

Schreibe ein Programm, dass in der folgenden Liste die längste Zeichenkette findet und ausgibt: 

```python
strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
```

Teste das Programm auch mit anderen Listen, die mehr unterschiedliche Elemente enthalten.
