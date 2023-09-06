matrix_mul = __import__('100-matrix_mul').matrix_mul

# 3 * 4
mat1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3]
]

# 4 * 2
mat2 = [
    [1, 2],
    [1, 2],
    [1, 2],
    [1, 2]
]

print(
    matrix_mul(mat1, mat2)
)