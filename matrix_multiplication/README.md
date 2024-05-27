# Matrix Multiplication

Matrix multiplication is one of the most trivial operations used in Data Science and Maths. The naive approach takes `O(n^3)` steps to compute the product of two matrices of input size `n`.
The Strassen's algorithm employs divide and conquer method to compute the product of two matrices. Each matrix is divided into sub-matrices and these sub-matrices are used to compute intermediate results using a sequence of operations (This sequence of operations involves computing 7 multiplication steps and a few addition and subtraction steps). The final results is then computed by combining all these intermediate results as shown below. 


A = [[A11, A12], [A21, A22]] Note - A11 is the upper left sub-matrix of size (n/2)*(n/2), and similarly others.
B = [[B11, B12], [B21, B22]]  

P1 = (A11 + A22)(B11 + B22)  
P2 = (A21 + A22)(B11)  
P3 = (A11)(B12 - B22)  
P4 = (A22)(-B11 + B21)  
P5 = (A11 + A12)(B22)  
P6 = (-A11 + A21)(B11 + B12)  
P7 = (A12 - A22)(B21 + B22)  

A * B = [ [ (P1 + P4 - P5 + P7) , (P3 + P5) ] , [ (P2 + P4) , (P1 - P2 + P3 + P6) ] ] 

## Time Complexity

* The algorithm converts each problem of size `n` into 7 subproblems of size `n/2`, compute the intermediate results, and then combine them using `O(n^2)` steps.
* The time complexity can be derived using the Master's theorem where a=7, b=2, and α = 2.
* Time complexity, `T(n) = ~n^2.81`


## Experimental Results

* Theorotically, the Strassen's algorithm is faster than the naive implementation, however, the actual implementation involves creation of sub-results and recursion. Hence, the implementation may ba slower than the naive approach for smaller input sizes.
* An efficient analysis isn’t measured in seconds but in how many basic steps it takes and how this scales when the size of the problem grows.
* The `matrix_multiplication.py` performs mulitplication of 2 `n*n` randomly initialised matrices, this is a basic implementation, it can be optimized using other packages to get better analysis.
* The `matrix_multiplication_v2.py` uses numpy package to do the same.

