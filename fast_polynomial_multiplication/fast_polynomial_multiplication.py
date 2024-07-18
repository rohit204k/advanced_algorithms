import cmath
import numpy as np

def nth_roots_of_unity(n, tolerance=1e-10):
    roots = []
    for k in range(n):
        theta = 2 * cmath.pi * k / n
        root = cmath.exp(1j * theta)
        
        if abs(root.imag) < tolerance:
            root = complex(root.real, 0)
        if abs(root.real) < tolerance:
            root = complex(0, root.imag)
        roots.append(root)
    return roots

def fft(A):
    if len(A) == 1:
        return [A[0]]
    
    else:
        A_even = A[0::2]
        A_odd = A[1::2]

        y_even = fft(A_even)
        y_odd = fft(A_odd)

        n = len(A)

        w = nth_roots_of_unity(n)
        y = [0]*n

        for k in range(n//2):
            y[k] = y_even[k] + w[k]*y_odd[k]

            y[k + n//2] = y_even[k] - w[k]*y_odd[k]

        return y
    
def fft_inverse(pvr_a, tolerance=1e-10):
    m = len(pvr_a)

    V_n_inverse = [[(1/m) for i in range(m)] for j in range(m)]

    theta = 2 * cmath.pi / m
        
    for i in range(m):
        for j in range(m):
            root = cmath.exp(1j * theta * (-1) * (i*j))
            if abs(root.imag) < tolerance:
                root = complex(root.real, 0)
            if abs(root.real) < tolerance:
                root = complex(0, root.imag)
            V_n_inverse[i][j] *= root
    
    A = [9 for i in range(m)]

    for i in range(m):
        a = 0
        for j in range(m):
            a+=V_n_inverse[i][j] * pvr_a[j]
        A[i] = a
    
    return A

def point_to_coefficients(points):
    """
    Convert the point value representation of a polynomial to its coefficient representation.

    Parameters:
    points (list or np.ndarray): The evaluations of the polynomial at the nth roots of unity.

    Returns:
    np.ndarray: The coefficients of the polynomial.
    """
    # Perform the inverse FFT to get the coefficient representation
    coefficients = fft_inverse(points)
    
    # Since the result might have small imaginary parts due to numerical errors,
    # take the real part (assuming the polynomial has real coefficients)
    coefficients = np.real_if_close(coefficients, tol=1e-9)
    
    return coefficients

def multiply(A, B):

    # degree = n - 1
    n = len(A)

    for i in range(n):
        A.append(0)
        B.append(0)

    pvr_a = fft(A)
    pvr_b = fft(B)
    
    pvr_c = [pvr_a[i]*pvr_b[i] for i in range(len(pvr_a))]

    c = point_to_coefficients(pvr_c)

    C = polynomial(c)

    return C
    # print(fft_inverse(pvr_c))

class polynomial():
    def __init__(self, coefficients) -> None:
        self.coefficients = coefficients
    
    def __str__(self) -> str:
        terms = []
    
        for i, coef in enumerate(self.coefficients):
            coef = int(coef)
            if coef == 0:
                continue
            
            term = ""
            
            # Handle the sign
            if coef > 0 and i != 0:
                term += "+ "
            elif coef < 0:
                term += "- "
            
            # Handle the coefficient
            abs_coef = abs(coef)
            if abs_coef != 1 or i == 0:
                term += str(abs_coef)
            
            # Handle the variable and exponent
            if i > 0:
                term += "x"
                if i > 1:
                    term += f"^{i}"
            
            terms.append(term)
    
        # Join the terms with spaces
        polynomial = " ".join(terms)

        return polynomial

def main():
    A = polynomial([1,2])
    B = polynomial([4,4])

    print('A :', A)
    print('B :', B)

    C =  multiply(A.coefficients, B.coefficients)

    print('Performing fast polynomial multiplication on A and B')
    print('C: ', C)

if __name__ == "__main__":
    main()

