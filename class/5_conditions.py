temperatur = int(input("Was ist die Temperatur heute? "))

if temperatur > 30:
   print("Es ist heiß.")
elif temperatur > 20:
   print("Es ist warm.")
elif temperatur <= -10:
   print("Es ist sehr kalt.")
elif temperatur <= 0:
   print("Es ist kalt.")
else:
   print("Es ist OK.")

'''
condition = False

if condition == True:
    print("Die Bedingung ist wahr.")
else:
    print("Die Bedingung ist falsch.")

print("Ende des Programms.")
'''