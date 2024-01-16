# Eine leere Liste erstellen
emptylist = []

# Eine String-Liste erstellen, jedes Element in dieser Liste ist eine Zeichenkette
stringlist = ["hello", "hi", "hallo", "hola"]

# Das zweite Element aus der Liste ausgeben, Index = 1
print(stringlist[1])

# Die Laenge der Liste messen: Wieviel Elemente gibt es in der Liste?
print(len(stringlist))

# Die ganze Liste ausgeben
print(stringlist)

# Gebe jedes Element aus der List aus
for element in stringlist:
    print(element)

# Fuehre bestimmte Logik fuer jedes Element in der Liste aus.
for element in stringlist:
    print(f"Der Originalwert der Variable ist: {element}.")
    print(element.capitalize())
    print(element.upper())
