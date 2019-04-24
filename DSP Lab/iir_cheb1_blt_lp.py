
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
j = cmath.sqrt(-1)

def iir_cheb1_lp_blt(wp,ws,delp,dels,ts):
	t = 2/ts
	#analog frequency calculation
	omp = t*math.tan(wp/2)
	oms = t*math.tan(ws/2)
	#order of the filter
	n1 = np.arccosh(math.sqrt((dels**(-2)-1)/(delp**(-2)-1)))
	n2 = np.arccosh(oms/omp)
	print n1/n2,omp,oms
	n = np.ceil(n1/n2)
	ni = n
	n = int(n)
	print n
	w = np.linspace(0,np.pi,1000)
	h = np.zeros(shape=(1000,),dtype=complex)
	ep = math.sqrt((delp**(-2))-1)
	x = math.sqrt(1+(ep**-2))+(1/ep)
	ni = 1/ni
	yn = 0.5*((x**ni)-(x**(-ni)))
	print yn,x,n
	if (n%2 == 0):
		z = np.exp(j*w)
		#for i in range(0,1000):
		s = t*((z-1)/(z+1))
		#s = (omp**2)/s                 uncomment for highpass filter
		pr = 1 
		prck = 1
		for k in range(1,((n/2)+1)):
			ck = (yn**2)+((math.cos(((2*k-1)*np.pi)/(2*n)))**2)
			bk = 2*yn*(math.sin((2*k-1)*np.pi/(2*n)))
			print ck,bk
			prck = prck * ck
			pr = pr*((s**2)+(bk*omp*s)+((omp**2)*ck))
		h = ((omp**n)*prck*delp)/pr
	else:
		z = np.exp(j*w)
		for i in range(0,1000):
			s = t*((z[i]-1)/(z[i]+1))
			#s = (omp**2)/s             uncomment for highpass filter
			pr = s+(omp*yn)
			prck = yn
			for k in range(1,((n-1)/2)+1):
				ck = (yn**2)+((math.cos(((2*k-1)*np.pi)/(2*n)))**2)
				bk = 2*yn*(math.sin((2*k-1)*np.pi/(2*n)))
				#print ck,bk
				prck = prck * ck
				pr = pr*((s**2)+(bk*omp*s)+((omp**2)*ck))
			h[i] = ((omp**n)*prck)/pr

	return h
	
k2 = iir_cheb1_lp_blt(0.35*np.pi,0.7*np.pi,0.8,0.2,1)
w = np.linspace(0,np.pi,1000)
m = np.abs(k2)
#m = m/max(m)
#print m
plt.plot(w,m)
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.show()


