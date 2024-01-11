
one_is_less_than_two = 1 < 2
true_equals_false = True == False

# python verwendet den Wert None, um auf nicht existente Werte hinzuweisen
x = None
assert x == None, 'this is not the pythonic /Pythoncommunity way to check for none'
assert x is None, ' this is the Pythonic way toy check for none'

# Python gestattet es, beliebiege Werte für einen boolschen Wert einzusetzten
# Alle folgenden Werte gelten als False

False
None
[]  # (eine leere Liste)
{}  # eine leeres Dictionary
""
set()
0
0.0

# Python kennt die Funktion all, die ein Iterable als Argument annimmt
# und True genau dann zurückgibt, wenn jedes einzelne Element wahr ist.
# Es gibt auch noch die Funktion any, die True liefert, sobald mindestens
# ein Element wahr ist:
all([True, 1, {3}])     # True, alle sind True
all([True, 1, {}])      # False, {} entspricht False
any([True, 1, {}])      # True, True ist True
all([])                 # True, lein Element der Liste entspricht False
any([])                 # False, kein Element der Liste entspricht True