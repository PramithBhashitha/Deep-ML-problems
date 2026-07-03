import numpy as np

def matrixmul(A, B):
    # Convert inputs to numpy arrays to access .shape
    A = np.array(A)
    B = np.array(B)
    
    # A.shape[1] is the number of columns in A
    # B.shape[0] is the number of rows in B
    if A.shape[1] == B.shape[0]:
        return A @ B  # Or np.matmul(A, B)
    else:
        return -1