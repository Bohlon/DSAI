from typing import Callable
import numpy as np
from typing import List
import random

Matrix = List[List[float]]
# Vector = np.array
Vector = List[float]
# Matrix = np.array

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int],float]) -> Matrix:
    return [[entry_fn(i,j)           
            for j in range(num_cols)]
            for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]

def shape(A: Matrix, j: int) -> Vector:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

assert make_matrix(4, 4, lambda i,j: 5) == [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]
assert make_matrix(4, 4, lambda i,j: 3) == [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]
assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"
assert shape([[1,2,3], [4,5,6]]) == (2,3)
assert identity_matrix(5) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]