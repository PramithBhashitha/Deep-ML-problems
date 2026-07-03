import numpy as np
def calculate_covariance_matrix(vectors):
	a=np.array(vectors)
	b=np.cov(a)
	return b