import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,1,0],[0,1,0],[0,0,1]])


(m_a,n_a) = a.shape
(m_b,n_b) = b.shape

if (n_a == m_b):
	c = np.empty(shape = (m_a,n_b)) 
	for i in range(0,m_a):
		for k in range(0,n_b):
			sum_ = 0
			for h in range(0,n_a):
				sum_ += (a[i,h]*b[h,k])
			c[i,k] = sum_
print c
