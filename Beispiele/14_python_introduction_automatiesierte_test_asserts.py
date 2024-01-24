# Assert-Anweisungen können dafür sorgen,
# dass der Code einen AssertError wirft,
# wenn die angegebenen Bedingungen nicht erfüllt sind

assert 1+1==2
assert 1+1==2,   "1+1 should equal 2 but didn't"

# Mit assert Anweisungen soll sichergestellt werden, dass eine geschriebene Funktion das tut, was man von ihr verlangt
def smallest_item(xs:list[int])->int:
    return min(xs)

assert smallest_item([10, 20, 57, 40]) == 10
assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1
assert smallest_item([1, 0, -1, -2]) == -1, 'somthing wrong with the smallest item'

# Asserts kommen auch bei Eingabewerten von Funktionen zum Einsatz
def smallest_item(xs:list)->int:
    assert xs, 'empty list has not samllest item'
    return min(xs)

smallest_item({12, 23})
smallest_item([])