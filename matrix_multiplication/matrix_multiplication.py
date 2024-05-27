import random
import time


def print_matrix(matrix):

    max_width = max(len(str(element)) for row in matrix for element in row)

    for row in matrix:
        print(" ".join(f"{str(element).rjust(max_width)}" for element in row))


def naive_matrix_multiplication(A, B):

    n = len(A)

    C = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


def add_matrix(A, B):
    n = len(A)

    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub_matrix(A, B):
    n = len(A)

    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def combine_matrices(a11, a12, a21, a22):
    n = len(a11)
    
    for i in range(n):
        a11[i].extend(a12[i])
        a21[i].extend(a22[i])
    
    a11.extend(a21)

    return a11


def strassen_matrix_multiplication(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        mid = n // 2
        a11 = [row[:mid] for row in A[:mid]]
        a12 = [row[mid:] for row in A[:mid]]
        a21 = [row[:mid] for row in A[mid:]]
        a22 = [row[mid:] for row in A[mid:]]

        b11 = [row[:mid] for row in B[:mid]]
        b12 = [row[mid:] for row in B[:mid]]
        b21 = [row[:mid] for row in B[mid:]]
        b22 = [row[mid:] for row in B[mid:]]

        p1 = strassen_matrix_multiplication(add_matrix(a11, a22), add_matrix(b11, b22))
        p2 = strassen_matrix_multiplication(add_matrix(a21, a22), b11)
        p3 = strassen_matrix_multiplication(a11, sub_matrix(b12, b22))
        p4 = strassen_matrix_multiplication(a22, sub_matrix(b21, b11))
        p5 = strassen_matrix_multiplication(add_matrix(a11, a12), b22)
        p6 = strassen_matrix_multiplication(sub_matrix(a21, a11), add_matrix(b11, b12))
        p7 = strassen_matrix_multiplication(sub_matrix(a12, a22), add_matrix(b21, b22))

        C = combine_matrices(
            add_matrix(sub_matrix(add_matrix(p1, p4), p5), p7),
            add_matrix(p3, p5),
            add_matrix(p2, p4),
            add_matrix(add_matrix(sub_matrix(p1, p2), p3), p6),
        )
    
        return C


def main():
    print("Matrix Multiplication")
    n = 512
    print(f"n = {n}")

    A = [random.choices(range(1, 11), k=n) for i in range(n)]
    # print("A = ")
    # print_matrix(A)
    # print()

    B = [random.choices(range(1, 11), k=n) for i in range(n)]
    # print("B = ")
    # print_matrix(B)
    # print()

    start = time.time()
    C1 = naive_matrix_multiplication(A, B)
    stop = time.time()
    normal_time = stop - start
    
    print('Naive Implementation O(n^3)')
    # print("A*B = ")
    # print_matrix(C1)
    # print()
    print(f'Time taken = {normal_time}')

    start = time.time()
    C2 = strassen_matrix_multiplication(A, B)  
    stop = time.time()
    strassen_time = stop - start

    print('Strassen\'s Algorithm Implementation O(n^2.81)')
    # print("A*B = ")
    # print_matrix(C2)
    # print()
    print(f'Time taken = {strassen_time}')

if __name__ == "__main__":
    main()
