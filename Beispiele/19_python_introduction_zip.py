# Häufig werden zwei oder mehr Iterables mit ZIP zusammengefügt.
# Die Funktion zip transformiert mehrere Iterables zu einem einzigen
# Iterable von Tupeln der korrespondierenden Funktion

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

[pair for pair in zip(list1, list2)]    # [('a': 1), ('b', 2), (c', 3)]

languages = ['Java', 'Python', 'Javascript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result)) # [('Java', 14), ('Python', 3), ('Javascript', 6)]

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
pairs = zip(numbers, letters)
print([*pairs])

numbers = [1, 2]
letters = ['a', 'b']
pairs = zip(numbers, letters)
print(*pairs)

pairs=[('a',1),('b',2),('c',3)] # Das Sternsymbol (*) führt das Entpacken von Argumenten durch
letters,numbers=zip(*pairs) # letters = ('a', 'b', 'c')
letters, numbers = zip(('a',1),('b',2),('c',3))


def add(a, b) -> int:
    return a + b

try:
    add([1, 2])
except TypeError:
    print('add expects 2 inputs')
    res = add(*[1, 2])
    print(res)
    