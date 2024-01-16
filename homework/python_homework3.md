## Python HA 3

### Aufgabe 2 (20 Punkte)
Erstelle eine Funktion `circle_area`, die den Radius eines Kreises als Parameter verwendet und dessen Fläche zurückgibt. (Verwende 3,14 als Wert von Pi).

### Aufgabe 2 (20 Punkte)

Schreibe eine Funktion mit dem Namen `print_many_times(text, times)`, die einen String und eine Ganzzahl als Argumente akzeptiert. Das Integer-Argument gibt an, wie oft das String-Argument ausgedruckt werden soll:

Beispielaufrufe:

```python
print_many_times("hi", 5)

print()

text = "All Pythons, except one, grow up"
times = 3
print_many_times(text, times)
```

Beispielausgabe:

```shell
hi
hi
hi
hi
hi

All Pythons, except one, grow up.
All Pythons, except one, grow up.
All Pythons, except one, grow up.
```

### Aufgabe 3 (30 Punkte)
Schreibe eine Funktion namens same_chars, die einen String und zwei Ganzzahlen als Argumente akzeptiert. Die Ganzzahlen beziehen sich auf Indizes innerhalb der Zeichenfolge. Die Funktion sollte „True“ zurückgeben, wenn die beiden Zeichen an den angegebenen Indizes identisch sind. Andernfalls und insbesondere wenn einer der Indizes außerhalb des Gültigkeitsbereichs der Zeichenfolge liegt, gibt die Funktion „False“ zurück.

Beispielaufrufe und Ausgabe:

```python
# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False
```

### Aufgabe 4 (30 Punkte)
Schreibe drei Funktionen: `erstes_Wort`, `zweites_Wort` und `letztes_Wort`. Jede Funktion benötigt ein String-Argument.

Wie der Name schon sagt, geben die Funktionen entweder das erste, das zweite oder das letzte Wort des Satzes zurück, den sie als String-Argument erhalten.

In jedem Fall kannst du davon ausgehen, dass die Argumentzeichenkette mindestens zwei separate Wörter enthält und alle Wörter durch genau ein Leerzeichen getrennt sind. Am Anfang und Ende der Argumentzeichenketten dürfen keine Leerzeichen stehen.

Beispielaufrufe und Ausgabe:

```python
print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python
```

## Extra Aufgaben für Extra Punkte 

### Extra 1 (40 Punkte)
Erstelle eine Funktion „validate_password“, die anhand dieser Kriterien prüft, ob ein Passwort gültig ist: 
- mindestens 8 Zeichen, 
- enthält einen Großbuchstaben, 
- einen Kleinbuchstaben 
- und eine Zahl. 

Die Funktion soll „True“ oder „False“ zurückgeben.

### Extra 2 (40 Punkte)
Schau dir den Code in der Datei `space_adventure.py` an. 
- Welcher Datentyp wird zur Implementierung von `locations` verwendet? 
- Wofür wird der Block `while True:` verwendet? 

Schreibe den Code so um, dass die Ausführung des Programms mit der `main()`-Funktion beginnt. Teste den Code.