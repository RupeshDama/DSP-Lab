import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
j = cmath.sqrt(-1)

def iir_but_blt_lp(wp,ws,delp,dels,ts):
	t = 2.0/ts
	omp = t*math.tan(wp/2)
	oms = t*math.tan(ws/2)
	n1 = math.log(((delp**-2)-1)/((dels**-2)-1))
	n2 = 2*math.log(omp/oms)
	ni = n1/n2
	n = int(ni)
	omc = omp/(((delp**(-2))-1)**(1/(2.0*n)))
	print oms,omp,omc,n
	h = np.zeros(shape=(1000,),dtype=complex)
	if (n%2 == 0):
		pr = 1
		w = np.linspace(0,np.pi,1000)
		z = np.exp(j*w)
		for i in range(0,1000):
			s = t*((z[i]-1)/(z[i]+1))
			for k in range(1,(n+2)/2):
				pr = pr*((s**2)+(2*omc*np.sin(((2*k)-1)*np.pi/(2*n)))+(omc**2))
			h[i] = (omc**n)/pr
		
	else:
		pr = s+omc
		w = np.linspace(0,np.pi,1000)
		z = np.exp(j*w)
		sk = t*((z-1)/(z+1))
		for i in range(0,1000):
			s = sk[i]	
			for k in range(1,(n+1)/2):
				pr = pr*((s**2)+(2*math.sin((2*k-1)*np.pi/(2*n))*omc)+(omc**2))
			h[i] = (omc**n)/pr
	return h
k2 = iir_but_blt_lp(1.1,1.6,0.8,0.1,0.1)
w = np.linspace(0,np.pi,1000)
m = np.abs(k2)
plt.plot(w,m)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()

















