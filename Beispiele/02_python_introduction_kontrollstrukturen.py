# Kontrollstrukturen
# wie in den meisten Programmiersprachen gibt es auch in Python eine IF Anweisung
if 1 > 2:
    message = 'if only 1 were greater than two...'
elif 1 > 3:
    message = "elif stands for 'else if'"
else: message = 'when all else fails use else...'


# man kann ternäre if-then-else Ausdrücke innerhalb einer Zeile schreiben
x = 3
partiy = 'even' if x % 2 == 0 else 'odd'

# Python kennt eine while-Schleife
x = 0
while x < 10:
    print(f'{x} is less than 10')
    x += 1

# Schleifen werden häufiger mit for und in eingesetzt
# range(10) liefert die Zahlen 0,1,....,9
for x in range(10):
    print(f'{x} is less than 10')

# Bei komplexen Flusskontrollenkann auch continue und break verwendet werden
for x in range(10):
    if x == 3:
        continue        # springe sofort zur nächsten Iteration
    if x == 5:
        break           # verlasse die Schleife
    print(x)

# Eine Match-Anweisung nimmt einen Ausdruck und vergleicht dessen Wert mit aufeinanderfolgenden Mustern,
# die als ein oder mehrere CASE-Blöcke angegeben sind
# Ab Python >= 3.10
status = 400
message = ''

match status:
    case 400:
        message = 'Bad Request'
    case 404:
        message = 'Not found'
    case 418:
        message = "I'm a teapot"
    case _:
        message = "Something's wrong with the internet"
print(message)