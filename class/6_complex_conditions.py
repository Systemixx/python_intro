benutzername = input("Benutzername: ")
passwort = input("Passwort: ")

# if benutzername == "admin" and passwort == "12345":
#     print("Zugriff erlaubt.")
# else:
#     print("Falscher Benutzername oder Passwort.")

if benutzername == "admin" or benutzername == "root" and passwort == "12345":
    print("Zugriff erlaubt.")
else:
    print("Falscher Benutzername oder Passwort.")