import numpy as np
from numpy import linalg as LA

def calculate_eigenvalues(matrix):

	a=np.array(matrix)
	calculate_eigenvalues=np.linalg.eigvals(a)

	return calculate_eigenvalues