# Eine weitere nützliche Datenstruktur ist das set, das eine Menge eindeutiger Elemente darstellt.
# Sets werden mit einer geschweiften Klammer definiert

primes_below_10 = {2,3,5,7}

# Achtung - funktioniert nicht für leere Sets, da {} für ein leeres dict steht.
# In dem Fall muss man set() benutzen
s = set()
s.add(1)            # s ist nun {1}
s.add(2)            # s ist nun {1,2}
s.add(2)            # s ist noch immer {1,2}
x = len(s)          # x gleich 2

y = 2 in s          # gleich true
z = 3 in s          # gleich false

# Sets werden hauptsächlich in zwei Sutuatuinen gebraucht
# * bei Verwendung von 'in' ... sehr schneller Vorgang
# * testen, ob ein bestimmtes Element enthalten ist (wesentlich besset als bei Listen)
item_list = [1,2,3,1,2,3]
num_items = len(item_list)      # 6
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)