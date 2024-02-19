import numpy as np


def matrix_multiplication():
    # 定义两个矩阵
    matrix_a = np.array([[1, 2],
                         [3, 4]])

    matrix_b = np.array([[5, 6],
                         [7, 8]])

    # 进行矩阵点乘
    result1 = np.dot(matrix_a, matrix_b)

    # 进行叉乘
    result2 = np.multiply(matrix_a, matrix_b)

    # 输出结果
    print("Matrix A:")
    print(matrix_a)
    print("Matrix B:")
    print(matrix_b)
    print("Matrix Dot Product (A x B):")
    print(result1)
    print("Matrix Multiply Product (A x B):")
    print(result2)


