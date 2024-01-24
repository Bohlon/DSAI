# In Data Science müssen häufig Zufallszahlen erzeugt werden
# Dies erfolgt mithilfe des Moduls random

import random
random.seed(10) # stellt sicher, dass wir immer die gleichen Ergebnisse bekommen

four_uniform_randoms = [random.random() for _ in range(4)]

random.random()

# Jeder Startwert entspricht einer Folge von generierten Werten
# D.h. wenn man zweimal denselben Startwert angibt, bekommt man dieselbe Zahlenfolge
random.seed(10)

# Die Funktion random.randrange() mit einem oder zwei Argumente
# gibt einen Zufallswert für eine range zurück
random.randrange(10)    # wähle zufällig aus range(10) = [0,...,9]
random.randrange(3,6)   # wähle zufällig aus range(3,6) = [3,4,5]

# Die Funktion random.shuffle() ordnet die Elemente einer Liste zufällig an
up_to_ten = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(up_to_ten)

# Die Funktion random.choice() wählt ein zufälliges Element aus einer Liste aus
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])

# Die Funktion ranom.sample() liefert Stichproben von Elementen ohne zurücklegen
lottery_numbers = range(1, 46)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

# Die Funktion random.choice() liefert Stichproben von Elementen mit zurücklegen
four_with_replacement = [random.choice(range(10)) for _ in range(4)]

# Zufallswerte mit Gewichtung
my_list = ["apple", "banana", "cherry"]
print(random.choices(my_list, weights=[0.5, 1, 1], k = 14))