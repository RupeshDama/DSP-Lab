import numpy as np
from matplotlib import pyplot as plt
def convolute(x,h):
    lx=len(x)
    lh=len(h)
    y=[]
    for n in range(lx+lh-1):
        sum=0
        for k in range(lx):
            if n-k<lh and n-k>=0:
                sum=sum+x[k]*h[n-k]
        y=np.append(y,sum)
    return y

def time_rev(x):
    lx=len(x)
    y=[]
    for i in range(0,lx):
	y=np.append(y,x[lx-i-1])
    return y

def correlate(x,h):
	x = np.asarray(x)
	h = np.asarray(h)
	hr = time_rev(h)
	y = convolute(x,hr)
	return y
x=np.array(input('enter seq1'))
h=np.array(input('enter seq2'))
print(convolute(x,h))
#print('conv=',np.convolve(x,h))
print(correlate(x,h))

