from typing import List
import math

Vector = List[float]

def add(v:Vector, w:Vector) -> Vector:
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def subtract(v:Vector, w:Vector) -> Vector:
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    num_elements = len(vectors[0])
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v:Vector, w:Vector) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v: Vector) -> float:
    return dot(v,v)

def magnitude(v: Vector):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector):
    return math.sqrt(squared_distance(v,w))

print(add ([1, 2, 3], [4, 5, 6]))

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
