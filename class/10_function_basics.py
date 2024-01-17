# 1. Basic Funktion
def greet_world():
    print("Hello, World!")

#greet_world()

# 2. Funktion - Definition mit einem Parameter
def greet_name(name):
    if type(name) == str:
        print(f"Hello, {name}!")
    else:
        print("Argument ungueltig.")

# Aufruf mit einem Argument
# greet_name("Alice")
# greet_name(3)
# greet_name(["Alice", "Bob", "Lucy"])
# new_name = "Bob"
# greet_name(new_name)

# 3. Funktion mit Rueckgabewert
def calculate_sum(a, b):
    """
    This function returns the sum of two numbers.
    Parameters:
        a (int): the first number
        b (int): the second number
    Returns:
        sum(int): The sum of two numbers a and b.
    """
    return a + b

# Den Rueckgabewert in einer Variable speichern
result = calculate_sum(5, 7)
print(result)
mult = result * 10
print(mult)
