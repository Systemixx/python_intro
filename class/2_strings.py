# Definiere eine Variable mit einer Zeichenkette als Wert
text = "This is my text."

# Gebe den Wert der text-Variable aus
print(text)

# Mehrere Text-Zeilen ausgeben: Beispiel 1
print("Zeile 1") 
print("Zeile 2")
print("Zeile 3")

# Mehrere Text-Zeilen ausgeben: Beispiel 2: \n als Zeilenumbruch
print("Zeile 1\nZeile 2\nZeile 3")

# Mehrere Text-Zeilen ausgeben: Beispiel 3: Multiline Strings

multiline_string = '''Zeile 1
Zeile 2
Zeile 3'''

print(multiline_string)

# String concatenation
part1 = "Hello"
part2 = "World"
result = part1 + " " + part2

print(result)

# Die Laenge einer Zeichenkette messen
length = len(result)

# Die str-Funktion transformiert andere Datentypen in Zeichenketten
print("Die Laenge der Zeichenkette '" + result + "' ist: " + str(length) + ".")

# Formatted Strings (formatierte Zeichenketten)
print(f"Die Laenge der Zeichenkette '{result}' ist: {length}.")

# Einzelne Zeichen aus der Zeichenkette ausgeben
print(part1[0])
print(part1[1])
print(part1[2])
print(part1[3])
print(part1[4])