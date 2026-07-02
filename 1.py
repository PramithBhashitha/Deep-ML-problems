import numpy as np

def matrix_dot_vector(matrix, vector):
    # Convert inputs to NumPy arrays
    matrix_arr = np.array(matrix)
    vector_arr = np.array(vector)
    
    # 1. Validate dimensions
    if matrix_arr.shape[1] != vector_arr.shape[0]:
        return -1  
        
    # 2. Compute dot product using the @ operator
    return (matrix_arr @ vector_arr).tolist()

## note
## matrix_arr.shape[1] - Gives the number of columns (index 1)
## vector_arr.shape[0] - Gives the length or number of elements in the vector (index 0)
## @ operator use for matrix multiplication. 
##