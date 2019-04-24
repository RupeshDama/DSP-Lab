import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as w

def disctft(a):
	a = np.asarray(a)
	l_aa = a.shape
	l_a = l_aa[0]
	print l_a
	p = np.pi
	w = np.linspace(-3.143j,3.143j,1000)
	l=1000
	y = np.zeros((l),dtype = complex)
	for k in range(l):
		s = 0
		for m in range(l_a):
			s = s+(a[m]*(np.exp(-(m*w[k]))))
		y[k]=s
	return y
n = np.arange(-3000,3000,1)
a = np.sin((np.pi)*n/2)
w = np.linspace(-3.143,3.143,1000)
b = disctft(a)
b_m = np.abs(b)
b_p = np.angle(b)
print b_m
plt.figure(1)
plt.plot(w,b_m)
plt.xlabel("---->frequncy in rad/sec")
plt.ylabel("---->magnnitude response")
plt.figure(2)
plt.plot(w,b_p)
plt.xlabel("---->frequncy in rad/sec")
plt.ylabel("---->phase response")
plt.show()

