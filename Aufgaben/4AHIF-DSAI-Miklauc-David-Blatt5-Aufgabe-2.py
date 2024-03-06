from typing import List
import numpy as np

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    return np.add(v, w)

def subtract(v: Vector, w: Vector) -> Vector:
    return np.subtract(v, w)

def vector_sum(vectors: List[Vector]) -> Vector:
    return np.sum(vectors, axis=0)

def scalar_multiply(c: float, v: Vector) -> Vector:
    return np.multiply(c, v)

def vector_mean(vectors: List[Vector]) -> Vector:
    return np.mean(vectors, axis=0)

def dot(v: Vector, w: Vector) -> float:
    return np.dot(v, w)

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

def magnitude(v: Vector) -> float:
    return np.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return np.sqrt(squared_distance(v, w))

print(add([1, 2, 3], [4, 5, 6]))
print(subtract([5, 7, 9], [4, 5, 6]))
print(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(scalar_multiply(2.5, [1, 2, 3, 4]))
print(vector_mean([[1, 2], [3, 4], [5, 6]]))
print(dot([1, 2, 3], [4, 5, 6]))
print(sum_of_squares([1, 2, 3]))
print(magnitude([3, 4]))
print(magnitude([-2, 3, 6]))
print(squared_distance([1, 2], [2, 3]))
print(distance([1, 2], [2, 3]))

assert np.array_equal(add([1, 2, 3], [4, 5, 6]), np.array([5, 7, 9]))
assert np.array_equal(subtract([5, 7, 9], [4, 5, 6]), np.array([1, 2, 3]))
assert np.array_equal(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]), np.array([16, 20]))
assert np.array_equal(scalar_multiply(2.5, [1, 2, 3, 4]), np.array([2.5, 5.0, 7.5, 10.0]))
assert np.array_equal(vector_mean([[1, 2], [3, 4], [5, 6]]), np.array([3, 4]))
assert dot([1, 2, 3], [4, 5, 6]) == 32
assert sum_of_squares([1, 2, 3]) == 14
assert magnitude([3, 4]) == 5
assert magnitude([-2, 3, 6]) == 7
assert squared_distance([1, 2], [2, 3]) == 2
assert distance([1, 2], [2, 3]) == 1.4142135623730951