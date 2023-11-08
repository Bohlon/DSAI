################################################################
# Tupel
# Tupel sind unveränderbare Cousins der Liste
# Tupel werden in runden Klammern geschrieben
# oder ganz ohne Klammern

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3

try:
    my_tuple[1]=3
except TypeError:
    print('cannot modify a tupel')

# Tupel ernöglichen es, bequem Funktionen mit mehreren Rückgabewerten zu schreiben
def sum_and_product(x:int,y:int)->tuple[int,int]:
    return (x+y),(x*y)

sp = sum_and_product(2,3)
s,p = sum_and_product(5,10)     # s ist 15, p ist 50

# Tupel (und Listen) können auch für Mehrfachzuweisungen verwendet werden
x,y = 1,2

# nun ist x gleich 1, y ist 2
x,y = y,x
