from typing import List
import math
import numpy as np

Vector = List[float]

def add(v:Vector, w:Vector) -> Vector:
    return [np.add(v, w)]

def subtract(v:Vector, w:Vector) -> Vector:
    return [np.subtract(v,w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    return [np.sum(vectors, axis=0)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    return [np.multiply(c, v)]

def vector_mean(vectors: List[Vector]) -> Vector:
    return [np.mean(vectors, axis=0)]

def dot(v:Vector, w:Vector) -> float:
    return np.dot(v, w)

def sum_of_squares(v: Vector) -> float:
    return dot(v,v)

def magnitude(v: Vector):
    return np.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector):
    return np.sqrt(squared_distance(v,w))

print(add([1, 2, 3], [4, 5, 6]))
print(subtract([5, 7, 9], [4, 5, 6]))
print(vector_sum ([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(scalar_multiply (2.5,[1, 2, 3, 4]))
print(vector_mean ([[1, 2], [3, 4], [5, 6]]))
print(dot([1, 2, 3], [4, 5, 6]))
print(sum_of_squares ([1, 2, 3]))
print(magnitude ([3, 4]))
print(magnitude ([-2,3,6]))
print(squared_distance ([1,2],[2,3]))
print(distance ([1,2],[2,3]))

assert add ([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert subtract ([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert vector_sum ([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert scalar_multiply (2.5,[1, 2, 3, 4]) == [2.5, 5.0, 7.5, 10.0]
assert vector_mean ([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot ([1, 2, 3], [4, 5, 6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6
assert sum_of_squares ([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3
assert magnitude ([3, 4]) == 5
assert magnitude ([-2,3,6]) == 7
assert squared_distance ([1,2],[2,3]) == 2
assert distance ([1,2],[2,3]) == 1.4142135623730951