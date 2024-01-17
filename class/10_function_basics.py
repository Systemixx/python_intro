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
# result = calculate_sum(5, 7)
# print(result)
# mult = result * 10
# print(mult)

# 4. Funktion mit Standardparametern
def power(base, exponent = 2):
    return base ** exponent

# result = power(3)
# print(result)
# result = power(3,3)
# print(result)
# result = power(2,8)
# print(result)

# 5. Funktion mit einer variablen Anzahl von Argumenten
def average(*numbers):
    return sum(numbers) / len(numbers)

# print(average(1,2,3,4))
# print(average(10,20,30))
# print(average(11,22,33,44,55,66,77,88,99))

# 6. Funktion mit mehreren Rueckgabewerten
def find_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = find_min_max([1, 2, 3, 4, 5])
#print(f"Minimum: {minimum}, Maximum: {maximum}")

minimum, maximum = find_min_max([100, 2, 30, 4000, 555])
#print(f"Minimum: {minimum}, Maximum: {maximum}")

# 7. Funktion mit Schluesselwortargumenten
def print_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# print_details(name="Alice", age=30, city="New York")
# print_details(city="Berlin", name="Bob", age=35)

def flexible_function(*args, **kwargs):
    print(args)
    for arg in args:
        print(f"Argument: {arg}")
    print(kwargs)    
    for key, value in kwargs.items():
        print(f"KW-Argument: Key '{key}', Value '{value}'")

flexible_function(1, 2, 3, name="Alice", age=30)
flexible_function(4, "number", [], 5, config="enabled")