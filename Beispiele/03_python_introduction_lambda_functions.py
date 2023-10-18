###########################################################
# Eine Funtion ist eine Regel, die null oder mehrere Eingabewerte
# annimmt und eine entsprechende Ausgabe zurückgibt.
# In Python definieren wir Funktionen üblicherweise mit def.
###########################################################

def double(x:int)->int:
    """An dieser Stelle kann ein optionaler Docstring stehen, der erklärt, was die Funktion tut.
    Diese Funktion multipliziert die Eingabe mit 2"""
    return 2*x

print(double(4))

y = double(3)
print(y)

# Alle Funktionen in Python sind First.Class-Funktionen, deswegen dürfen wir sie zuweisen
# oder anderen Funktionen als Argumenten übergeben.

def apply_to_one(f):
    """Ruft die Funktion f mit dem Argument 1 auf."""
    return f(1)

my_double = double # bezieht sich auf die zuvor definierte Funktion
x = apply_to_one(my_double)
print(x)

# Darüber hinaus kann man kurze anonyme Funktionen oder Lambdas erstellen
y = apply_to_one(lambda x: x+4)     # => 5
print(y)
# Man kann Lambdas auch Variablen zuweisen
another_double = lambda x: 2*x

# Bei den Argumenten von Funktionen lassen sich Werte voreinstellen,
# sodass Sie die Argumente nur angeben müssen, wenn Sie sich andere als Standardwert wünschen

def my_print(message = 'my default message'):
    print(message)

my_print('hello')   # gibt 'hello' aus, kein fefaultwert
my_print()          # gibt 'my default message' aus

# Oft ist es nützlich, die Namen von Argumenten mitzugeben

def full_name(first = "Firstname", last = 'Lastname'):
    return first + ' ' + last

full_name('David', 'Miklauc')
full_name(last='Mayer')

# Function overloading is not supported by python
def area(l,b):
    pass
def area(r):
    pass
area(1)