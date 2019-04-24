import numpy as np
import cmath 
import math 
import matplotlib.pyplot as plt
j = cmath.sqrt(-1)

def iir_but_blt_hp(ws,wp,dels,delp,ts):
	t = 2.0/ts
	omp = t*math.tan(wp/2)
	oms = t*math.tan(ws/2)
	n1 = math.log(((delp**-1)-1)/((dels**-1)-1))
	n2 = 2*math.log(omp/oms)
	n = n1/n2
	n = math.ceil(n)
	n = int(n)
	print n
	omc = omp/(((delp**(-2))-1)**(1/n))
	print oms
	w = np.linspace(0,np.pi,1000)
	h = np.zeros((1000,),dtype = complex)
	if(n%2 == 0):
		z = np.exp(j*w)
		for k in range(0,1000):
			pr = 1
			sdash = t*((z[k]-1)/(z[k]+1))
			s = (omp**2)/sdash
			for i in range(1,(n/2)+1):
				x = math.sin(((2*i)-1)*np.pi/(2*n))
				pr = pr*((s**2)+(2*s*omc*x)+(omc**2))
			h[k] = (omc**n)/n
	else:
		
		z = np.exp(j*w)
		print z
		for k in range(0,1000):
			s = t*((z[k]-1)/(z[k]+1))
			pr = s+omc
			s = t*((z[k]-1)/(z[k]+1))
			for i in range(1,((n-1)/2)+1):
				x = math.sin(((2*i)-1)*np.pi/(2*n))
				pr = pr*((s**2)+(2*s*omc*x)+(omc**2))
			h[k] = (omc**n)/pr
				
	return h
	
k2 = iir_but_blt_hp(1.1,1.6,0.6,0.1,0.1)
w = np.linspace(0,np.pi,1000)
m = np.abs(k2)
print m
plt.plot(w,m)
plt.show()


