# Jede Liste in Python besitzt die Methode sort, die die enthaltenen Daten sortiert.
# Möchte man die Liste nicht verändern, kann die Funktion sorted verwendet werden, die 
# eine neue Liste zurückgibt.

x = [4, 1, 2, 3]
y = sorted(x)       # y = [1, 2, 3, 4], x ist unverändert
x.sort()            # nun ist x = [1, 2, 3, 4]

# Die Methoden 'sort' und 'sorted' sortiert eine Liste standardmäßig in aufsteigender Reihenfolge.
# Sie wird vom kleinsten Element zum größten Element sortiert, indem die Elemente miteinander verglichen werden.
# Wenn die Elemente in absteigender Reihenfolge sortiert werden sollte, wird der Parameter reverse-True gesetzt.
# Um ein Element selbst zu vergleichen, kann eine Funktion übergeben werden, bspw key

x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
word_counts = {'world': 2, 'hello': 12, 'is': 5, 'cool': 7}
wc = sorted(word_counts.items(), key = lambda word_and_count : word_and_count[1], reverse = True)