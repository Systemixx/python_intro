def convert_temperature(temp, unit):
    """
    This function returns the converted temperature.
    Parameters:
        temp (int): temperature
        unit (string): unit
    Returns:
        temperature(float): The converted temperature.
    """
    if unit == "F":
        return (temp - 32) * 5/9
    elif unit == "C":
        return temp * 9/5 + 32
    else:
        print("Unbekannte Messeinheit.")


def main():
    print("Welcome to Temperature Converter")
    temperature = int(input("Gib die Temperatur ein: "))
    einheit = input("Was ist die Messeinheit: C oder F ")
    result = convert_temperature(temperature, einheit)
    if einheit == "C":
        print(f"Die Temperatur in F ist : {result}")
    elif einheit == "F":
        print(f"Die Temperatur in C ist : {result}")
    else:
        print("Unbekannte Einheit.")


if __name__ == "__main__":
    main()