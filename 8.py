import numpy as np
from numpy import linalg as LA
def inverse_2x2(matrix):
    
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    
    det = a * d - b * c
    
    
    if det == 0:
        return None
        

    inv_matrix = np.linalg.inv(matrix)
    return inv_matrix