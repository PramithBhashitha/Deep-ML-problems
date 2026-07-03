import numpy as np
from numpy import linalg as LA
from numpy.linalg import multi_dot 
def transform_matrix(A,T,S):
	a=np.array(A)
	b=np.array(S)
	c=np.linalg.det(T)
	d=np.linalg.det(S)
	if c==0 or d==0 :
		return -1
	else:
		d=np.linalg.inv(T)
		return d.dot(a).dot(b)
