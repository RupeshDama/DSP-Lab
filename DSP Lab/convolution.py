import numpy as np

def shift_arr(a,k):
	a = np.asarray(a)
	len_a = a.shape
	la = len_a[0]
	for i in range(0,la):
		if(la-1-i<=k):
			for i in range(0,k):
				a[i] = 0
			break
		a[la-i-1] = a[la-i-k-1]
	return a
	
def add_zeroes(a,l):
	a = np.asarray(a)
	len_a = a.shape
	la = len_a[0]
	y = l-la
	c = np.zeros(y)
	a = np.append(a,c)
	return a

			
def conov(a,b):
	a = np.asarray(a)
	b = np.asarray(b)
	len_a = a.shape
	len_b = b.shape
	la = len_a[0]
	lb = len_b[0]
	ly = la+lb-1
	a=add_zeroes(a,ly)
	b=add_zeroes(b,ly)
	y = np.zeros(ly)
	for i in range(lb):
		sh_a = shift_arr(a,i)
		print a,b[i],y
		y = y+(b[i]*sh_a)
	return y
	
a = [1,1,1,1,1]
b = [1,1,1]
k = conov(a,b)
k_func = np.convolve(a,b)

print "from my code == ",k
print "from default function == ",k_func

	
