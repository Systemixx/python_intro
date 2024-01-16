# Liste von Zahlen
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_multiplied = []

# Jede Zahl aus der Liste ausgeben, transformieren und in eine neue Liste speichern
for num in numbers:
    print(num)
    result = num * 10
    numbers_multiplied.append(result)

for num in numbers_multiplied:
    print(num)

# Gerade Zahlen berechnen und in eine neue Liste hinzufuegen

gerade_zahlen = []

for zahl in range(1,21):
    if zahl % 2 == 0:
        print(f"{zahl} ist gerade")
        gerade_zahlen.append(zahl)
    else:
        print(f"{zahl} ist ungerade")

print(gerade_zahlen)





