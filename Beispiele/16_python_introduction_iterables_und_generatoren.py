# Bei Listen kann man spezifsche Elemente über ihren Index aufrufen
# Dies wird jedoch nicht immer benötigt
# Eine Liste mit einer Milliarde Zahlen verbraucht viel Speicher.
# Wollen Sie die Elemente immer nur nacheinander nutzen,
# gibt es keinen Grund dafür, sie alle gleichzeitig vorzuhalten.
# Benötigen Sie schließlich nur die ersten Elemente,
# ist das Erzeugen der gesamten Milliarden Einträge eine Verschwendung.
# Häufig muss man über die Kollektion nur per for und in iterieren.
# In diesem Fall können wir Generatoren erstellen, über die wie über Listen
# iterier werden kann, die ihre Werte erst dann produzieren,
# wenn diese gebraucht werden

# Eine Möglichkeit zum Erstellen von Generatoren sind Funktionen
# mit dem Operator yield:

def generate_range(n:int) -> int:
    i:int = 0
    while i < n:
        yield i     # Jeder Aufruf von yield erzeugt einen Wert des Generators
        i += 1

# Die folgende Schleife bearbeitet die durch yield produzierten Werte
# einem nach dem Anderen, bis keine mehr übrig sind
for i in generate_range(10):
    print(f'i: {i}')

# odd range
def generate_range_odd(n:int) -> int:
        i:int = 1
        while i < n:
            yield i     # Jeder Aufruf von yield erzeugt einen Wert des Generators
            i += 2
for i in generate_range_odd(99):
    print(f'i: {i}')

# Mir einem Generator kann man sogar unendliche Zahlenfolgen erzeugen:
def natural_numbers() -> int:
    """ returns 1,2,3,..."""
    n = 1
    while True:
        yield n 
        n += 1

n = natural_numbers()
n.__next__()
n.__next__()
n.__next__()
# Achtung Abbruchbedingung ist unbeding erforderlich
# z.B. mittels break einbauen

# Eine andere Möglichkeit zum Erzeugen von Generatoren bieten
# in runden Klammern eingeschlossene for-Comprehensions:
lazy_even_below_20 = (i for i in generate_range(20) if i%2 == 0)    # verzögert Zahlen

# Solch ein Generator tut gar nichts, bis man darüber iteriert
# mir Hilfe von for oder next
data = natural_numbers()    # tut solange nicht, bis er aufgerufen wurde
evens = (x for x in data if x%2 == 0)   # tut solange nicht, bis er aufgerufen wurde 
even_squares = (x**2 for x in evens)    # tut solange nicht, bis er aufgerufen wurde 
even_squares_ending_in_six = (x for x in even_squares if x%10 == 6)

# Pythonesk
# Die Funktion enumerate() fügt einen Zähler als Schlüssel
# des Aufzählungsobjekts hinzu
names = ["Alice", "Bob", "Charlie", "Debbie"]
for i, name in enumerate(names):
    print(f'name {i} is {name}')

# nicht nach Pythonesk, don't do it!
i = 0
for name in names:
    print(f'name {i} is {names[i]}')
    i += 1
