########################################################################
# Wichtige Datenstruktur in Python ist die Liste (list)
# Eine Liste ist einfach eine geordnete Abfolge von Elementen
# Sie ähnelt Arrays in anderen Sprachen, bietet aber zusätzliche Funktionen

integer_list = [1,2,3]
hetereogeneous_list = ["string",0.1,True]
list_of_list = [integer_list, hetereogeneous_list,[]]
list_length = len(integer_list)     # gleich 3
list_sum = sum(integer_list)        # gleich 6

x = [-1,1,2,3,4,5,6,7,8,9]
nine = x[-1]

# Slicing 
# Man kann eckige Klammern auch einsetzen, um Listen in Scheiben zu zerschneiden (slide)
# Der Slice i:j bezieht sich auf alle Elemente von i (EINSCHLIESSLICH) bis j (NICHT EINSCHLIESSLICH)
# Lässt man den Anfang des Slice weg, schneidet man alles vom Anfang der Listen aus
# Lässt man das Ende weg, schneidet man bis zum Ende der Liste aus
first_three = x[:3]                 # [-1,1,2]
three_to_end = x[3:]                # [3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_last_three = x[:-3]         # [-1, 1, 2, 3, 4, 5, 6]
without_first_and_last = x[1:-1]    # [1, 2, 3, 4, 5, 6, 7, 8]
copy_of_x = x[:]
not_a_copy_of_x = x

# Man kann auch Strings und andere "sequentielle Typen" zerteilen
hello:str = 'Hello World'
hello[-3:]                          # 'rld'

# Einem Slice kann ein drittes Argument mitgegeben werden, dabei handelt es sich um die Schrittweite, die Schrittweite 
# kann auch negative sein
every_third = x[::3]                # [-1,3,6,9]
five_to_three = x[5:2:-1]           # [5,4,3]

# Python kennt den Operator 'in' zum Prüfen der Mitgliedschaft in einer Liste
1 in [1,2,3]                        # True
0 in [1,2,3]                        # False

x = [1,2,3]                         # [1,2,3]
y = x + [4,5,6]                     # [1,2,3,4,5,6]

# Element nach dem anderen an Liste anhängen
x = [1,2,3]
x.append(0)                         # [1,2,3,0]
z = len(x)                          # gleich 4

# Entpacken einer Liste falls die Anzahl der Werte bekannt ist
x,y = [1,2]                         # nun ist x gleich 1, y ist 2
x = [1,2]

# Es ist üblich, einen Unterstrich zu machen für nicht benötigte Werte
_,y = [1,2]                         # y ist gleich 2
_,_,y,_ = [1,2,3,4]                 # y ist gleich 3
