######################################################
# List Comprehension
# Listen müssen häufig in andere Listen umgewandelt werden,
# indem man nur bestimmte Elemente auswählt, Elemente gezielt umwandelt oder beides.
# Die in Python übliche Bezeichnung hierfür lautet List Comprehension.

even_numbers = [x for x in range(5) if x % 2 == 0]    # [0, 2, 4]
squares = [x * x for x in range(5)]                   # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]          # [0, 4, 16]

# Dies ist in ähnlicherweise auch mit Listen und Dictionaries oder Sets möglich.
square_dict = {x : x * x for x in range(5)}         # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set = {x * x for x in [1, -1]}               # {1}

# Wenn die Werte aus der Liste nicht benötigt werden, ist es üblich, einen Unterstrich
# als Variablennamen zu Verwenden
zeros = [0 for _ in even_numbers]                   # hat die gleiche Länge wie even_numbers

# Eine List Comprehension kann mehere for-Schleifen enthalten:
pairs = [(x,y) for x in range(10) for y in range(10)]   # [(0,0), (0,1)...]

# Dabei können die späteren for-Schleifen die Laufvariablen der vorangegangenen verwenden
increasing_pairs = [(x,y) 
                    for x in range(4)
                    for y in range(x + 1, 3)]

# Python list comprehension using if statement
num = [i for i in range(10) if i % 2 == 0]              # [0, 2, 4, 6, 8]
print(num)

# Python list comprehensions using if 
num = num = [i for i in range(10) if i >= 5]            # [5, 6, 7, 8, 9]
print(num)

# Python list comprehension using nested if statement
num = [i for i in range(20) if i%2 == 0 if i % 3 == 0]    # [0, 6, 12, 18]
print(num)

# Python list comprehension using multiple if statements
num = [i for i in range(30) if i>= 2 if i <= 25 if i % 4 == 0 if i % 8 == 0]
print(num)

# Python list comprehension using if-else
fruits = ['mango' if i % 3 == 0 else 'orange' for i in range(10)]
print(fruits)

# Python list comprehension using nested for loop
for i in range(2,4):
    for j in range(1,5):
        print(f'{i} + {j}')

# Python list comprehension transposes rows and columns
matrix = [[1,2], [3,4], [5,6], [7,8]]
# tmp = [[row[i] for row in matrix] for i in range(2)]      # entweder so (ohne externe for)
tmp = []                                                    # oder so
for i in range(2):
    tmp.append([row[i] for row in matrix])
print(tmp)

