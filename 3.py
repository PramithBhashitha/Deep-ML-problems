import numpy as np

def reshape_matrix(a,new_shape):

    tot_elements_a=np.size(a)
    tot_elements_new_shape=np.prod(new_shape)

    if tot_elements_a==tot_elements_new_shape:
        return np.reshape(a,new_shape).tolist()
    else:
        return []