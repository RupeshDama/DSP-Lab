import numpy as np
import matplotlib.pyplot as plt
print("values for first wave")
f = input("enter frequency")
phi_deg = input("enter phase shift in degrees")
dc = input("enter if wave has a D.C value")
a1 = input("amplitude")

f = np.float16(f)  
k = np.float16(np.pi)

phi_rad = (phi_deg*k)/180   #changing phase shift in degrees to radians
tp = 1/f                    #time period of wave

t = np.linspace((-5*tp),5*tp,250) #taking samples
y1 = dc+(a1*np.sin((2*k*f*t)+phi_rad))

print("values for second sinusoidal wave")

f2 = input("enter frequency")
phi_deg2 = input("enter phase shift in degrees")
dc2 = input("enter if wave has a D.C value")
a2 = input("amplitude")

f2 = np.float16(f)  
k2 = np.float16(np.pi)

phi_rad2 = (phi_deg2*k2)/180   #changing phase shift in degrees to radians
tp2 = 1/f2                    #time period of wave

t2 = np.linspace((-5*tp2),5*tp2,250) #taking samples
y2 = dc2+(a2*np.cos((2*k2*f2*t2)+phi_rad2))

plt.subplot(3,1,1)
plt.plot(t,y1)
plt.subplot(3,1,2)
plt.plot(t2,y2)
plt.subplot(3,1,3)
plt.plot(t,y1+y2)
plt.show()
