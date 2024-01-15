# Benutzereingabe anfordern und in der Variable speichern
name = input("What is your name? ")
print(f"Hello, {name}!")

# Eingabe der ganzen Zahlen: Beispiel
print("Berechne die Summe von zwei ganzen Zahlen.")
number1 = int(input("Gebe die erste Zahl ein: "))
number2 = int(input("Gebe die zweite Zahl ein: "))

sum = number1 + number2

print(f"Die Summe ist: {sum}.")

# Eingabe der Gleitkommazahlen: Beispiel
print("Berechne die Summe von zwei Gleitkommazahlen.")
float1 = float(input("Gebe die erste Zahl ein: "))
float2 = float(input("Gebe die zweite Zahl ein: "))

float_sum = float1 + float2
print(f"Die Summe der Gleitkommazahlen ist: {float_sum}.")