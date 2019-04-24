import numpy as np
import matplotlib.pyplot as plt

def d_ft(a,N):
	a = np.asarray(a)
	l = a.shape
	n = l[0]
	ex = np.linspace(0,6.283185307j,N+1)
	#print ex
	b = np.zeros(shape=N,dtype=complex)
	for k in range(N):
			for h in range(n):
				if(h<N):
					b[k] = b[k]+(a[h]*np.exp(-1*ex[h]*k))
		
	return b
			
a = np.array(input("enter signal"))
n = input("no of points")
b = d_ft(a,n)
c = np.fft.fft(a,n)
print b
print c



