# Ein Counter wandelt eine Abfolge von Werten in ein
# defaultdict(in) ähnliches Objekt um, bei dem jedem Schlüssel eine Anzahl zugeordnet ist
from collections import Counter

c = Counter([0,1,1,1,2,0])      # Counter({1: 3, 0: 2, 2: 1})

# Eine Instanz von Counter besitzt die Methode most_common
# die die häufigsten Elemente liefert
for value, count in c.most_common(2):
    print(value, count)

# Gib die 10 häufigsten Wörter und deren Anzahl aus
document = ['heute ', 'ist', 'ein', 'schöner', 'Tag', 'und', 'morgen', 'ist', 'auch', 'ein', 'schöner', 'Tag'] 
words_count = Counter(document)

for word, count in words_count.most_common(10):
    print(word, count)