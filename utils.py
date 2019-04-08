import numpy as np

def to_one_hot(y):
	
	y_hot = np.eye(y.max()+1)[y]
	return y_hot