# Liste von Zahlen
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension: transformiere jedes Element aus der Originalliste und speichere das Ergebins in der neuen Liste
number_multiplied = [num * 10 for num in numbers]

print(number_multiplied)

# List Comprehension mit einer Bedingung: schreibe in die neue Liste nur die Elemente aus der Originalliste, die der Bedingung entsprechen
gerade_zahlen = [num for num in numbers if num % 2 == 0]

print(gerade_zahlen)

# Random List
random_list = [1, 4.3, "string"]

