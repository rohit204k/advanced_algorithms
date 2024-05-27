import numpy as np
import time

def print_matrix(matrix):

    max_width = max(len(str(element)) for row in matrix for element in row)

    for row in matrix:
        print(" ".join(f"{str(element).rjust(max_width)}" for element in row))

def naive_matrix_multiplication(A, B):

    n = A.shape[0]
    
    C = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    
    return C



def strassen_matrix_multiplication(A, B):
    n = A.shape[0]

    # base case: 1x1 matrix
    if n == 1:
        return A * B
    else:
        # split input matrices into quarters
        mid = n // 2
        A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
        B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

        # calculate p1 to p7
        P1 = strassen_matrix_multiplication(A11 + A22, B11 + B22)
        P2 = strassen_matrix_multiplication(A21 + A22, B11)
        P3 = strassen_matrix_multiplication(A11, B12 - B22)
        P4 = strassen_matrix_multiplication(A22, B21 - B11)
        P5 = strassen_matrix_multiplication(A11 + A12, B22)
        P6 = strassen_matrix_multiplication(A21 - A11, B11 + B12)
        P7 = strassen_matrix_multiplication(A12 - A22, B21 + B22)

        # calculate the 4 quarters of the resulting matrix
        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 + P3 - P2 + P6

        # combine the 4 quarters into a single result matrix
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

        return C

def main():
    print("Matrix Multiplication")
    n = 512
    print(f"n = {n}")

    A = np.random.randint(0, 11, size=(n, n))
    # print("A = ")
    # print_matrix(A)
    # print()

    B = np.random.randint(0, 11, size=(n, n))
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
