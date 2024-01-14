## Python HA 1

### Aufgabe 1 (10 Punkte)

Schreibe einen Python-Code, der den folgenden Text ausgibt:

```python
Lorem ipsum dolor sit amet. 
Consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt. 
Ut labore et dolore magna aliqua.
```

Jeder Satz muss in einer separaten Zeile ausgegeben werden.

### Aufgabe 2 (20 Punkte)

Öffne die Datei "ha1_aufgabe2_bugs.py" und behebe alle Fehler im Code.

### Aufgabe 3 (20 Punkte)

Schreibe einen Python-Code, der Benutzerdaten für das Adressbuch sammelt. Das Programm soll Benutzer interaktiv auffordern, ihren Vornamen, ihren Nachnamen, ihre Telefonnummer und ihre Adresse einzugeben. 

Beispielausgabe:

```shell
What is your first name?
Barbara
What is your last name?
Roberts
What is your telephone number?
+4915 555 555 555
What is your address?
Invalidenstr. 115 10115 Berlin
```

### Aufgabe 4 (30 Punkte)

Schreibe einen Python-Code, der die Anzahl der Buchstaben im Namen berechnet. Der Code sollte den Benutzer zur Eingabe auffordern und die Summe der Buchstaben im Vor- und Nachnamen des Benutzers berechnen.

Beispielausgabe:

```shell
What is your first name?
Barbara
What is your last name?
Roberts
There are 7 letters in your first name "Barbara".
There are 7 letters in your last name "Roberts".
There are 14 letters in total in your name.
```

### Aufgabe 5 (20 Punkte)

Schreibe einen Python-Code, der den Steuer von 19 % aus dem angegebenen Nettoproduktpreis sowie den Bruttopreis berechnet.

Beispielausgabe:

```shell
Please enter the netto product price: 100
The 19% tax is 19 Euro.
The brutto price is 110 Euro.
```

## Extra Aufgaben für Extra Punkte 

### Extra 1 (20 Punkte)

Schreibe ein Python-Programm, das die Ziffern einer zweistelligen Zahl addiert. z.B. Wenn die Eingabe 35 war, sollte die Ausgabe 3 + 5 = 8 sein.

### Extra 2 (20 Punkte)

Schreibe ein Programm, das den Body-Mass-Index (BMI) aus dem Gewicht und der Größe eines Benutzers berechnet. Die BMI-Formel findest du auf der Wikipedia-Seite: https://de.wikipedia.org/wiki/Body-Mass-Index 

### Extra 3 (30 Punkte)

Schreibe ein Programm, das berechnet, wie viele Wochen dir noch bleiben, bis du 90 Jahre alt wirst.
Es soll dein aktuelles Alter als Eingabe verwenden und eine Nachricht mit der verbleibenden Zeit in diesem Format ausgeben:

```shell
Sie haben noch x Wochen Zeit.
```

Dabei wird x durch die tatsächlich berechnete Anzahl der Wochen ersetzt, die dem eingegebenen Alter bis zum Alter von 90 Jahren verbleiben.

### Extra 4 (25 Punkte)

Schreibe ein Programm, das die typischen Lebensmittelausgaben eines Benutzers schätzt.

Das Programm fragt den Benutzer, wie oft pro Woche er in einem Restaurant isst. Dann wird nach dem Preis eines typischen Essens und nach dem Geld gefragt, das während der Woche für Lebensmittel ausgegeben wird.

Basierend auf diesen Informationen berechnet das Programm den typischen wöchentlichen und täglichen Lebensmittelverbrauch des Benutzers.

Beispielausgabe:

```shell
How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
```

### Extra 5 (25 Punkte)

Schreibe ein Programm, das nach der Anzahl der Studierenden eines Kurses und der gewünschten Gruppengröße fragt. Das Programm druckt dann die Anzahl der aus den Studenten des Kurses gebildeten Gruppen aus. Wenn die Aufteilung nicht gleichmäßig ist, hat eine der Gruppen möglicherweise weniger Mitglieder als angegeben.

Beispielausgabe:

```Shell
How many students on the course? 8
Desired group size? 4
Number of groups formed: 2

How many students on the course? 11
Desired group size? 3
Number of groups formed: 4
```