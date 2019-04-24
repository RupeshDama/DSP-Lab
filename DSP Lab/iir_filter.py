#25/03/2019
import numpy as np
import matplotlib.pyplot as plt
import cmath

j = cmath.sqrt(-1)


def iir_butt_blt(wp,ws,delp,dels,ts): #bilinear transformation
	oms = (2.0/ts)*(np.tan(0.5*ws))
	omp = (2.0/ts)*(np.tan(0.5*wp))
	nc1 = np.log((((dels**(-2.0))-1.0)/((delp**(-2.0))-1.0)))
	nc2 = np.log(oms/omp)
	nc  = (nc1/nc2)*0.5
	ni = np.ceil(nc)
	n = int(ni)
	omc = oms/((dels**(-2)-1)**(1/(2*ni)))
	w = np.linspace(0,3.143,1000)
	h = np.zeros(shape=(1000,),dtype = complex)
	w = np.linspace(0,np.pi,1000)
	z = np.exp(j*w)
	s = (2/ts)*((z-1)/(z+1))
	print oms,omp,omc,n
	if (n%2 == 0):
		pr = 1
		k1 = n/2
		for k in range(1,k1+1):
			pr = pr*((s**2)+(2*s*omc*np.cos(((2*k-1)*(np.pi))/(2*n)))+(omc**2))
		h = (omc**n)/pr
	else:
		pr = s+omc
		k1 = (n-1)/2
		for k in range(1,k1+1):
			pr = pr*((s**2)+(2*s*omc*np.cos(((2*k-1)*(np.pi))/(2*n)))+(omc**2))
		h = (omc**n)/pr
			
	return h

#wp = input("enter digital passband edge frq")
#ws = input("enter digital stopband start frq")
#delp = input("enter passband attenuation")
#dels = input("enter stopband attenuation")

k1 = np.empty(shape=(1000,))
k2 = iir_butt_blt(1.1,1.9,0.9,0.1,0.1)
w = np.linspace(0,3.143,1000)

km = np.abs(k2)
plt.plot(w,km)
plt.show()

print k1,k2

