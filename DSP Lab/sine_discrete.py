import numpy as np
import matplotlib.pyplot as plt

f = input("enter frequency")
phi_deg = input("enter phase shift in degrees")
dc = input("enter if wave has a D.C value")

f = np.float16(f)  
k = np.float16(np.pi)

phi_rad = (phi_deg*k)/180   #changing phase shift in degrees to radians
tp = 1/f 

n = np.linspace((-5*tp),5*tp,100) #taking samples
y = dc+np.sin((2*k*f*n)+phi_rad)

plt.stem(n,y)
plt.show()
