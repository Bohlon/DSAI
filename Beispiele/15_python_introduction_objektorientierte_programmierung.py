# In Python kann man Klassen defienieren, die Daten und 
# Funktionen zu deren Bearbeitung kapseln. Dies wird oft
# benötigt, um Code sauber zu halten

class CountingClicker:     # Name in Pascal Case Notation
    """
    Eine Klasse sollte wie jede Funktion einen Docstring haben
    """
    count_all: int = 0   # class variable shared über alle Instanzen
    def __init__(self, counter: int = 0)  -> None:
        self.count = counter    # Instanzvariable
        CountingClicker.count_all += 1     # static variable

    def __repr__(self) -> str:
        return f"CountingClicker(count={self.count})"   # str(class_instance)

    def click(self, num_times: int = 1) -> int:
        """ Den Zähler num_times gedrückt"""
        self.count += num_times

    def read(self) -> int:
        self.count
    
    def reset(self) -> None:
        self.count = 0

clicker = CountingClicker()
assert clicker.read() == 0, 'clicker should start with count 0'
clicker.click()
clicker.click()
assert clicker.read() == 2, 'after two clicks, clicker shouldnt have count 0'
clicker.reset()
assert clicker.read() == 0, 'after reset, clicker should be back to 0'

str(clicker)

## build-in Functions
getattr(CountingClicker, 'count_all')

clicker2 = CountingClicker()
clicker2.click()
getattr(CountingClicker, 'count_all')
clicker2.count