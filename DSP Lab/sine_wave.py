import numpy as np
import matplotlib.pyplot as plt

f = input("enter frequency")
phi_deg = input("enter phase shift in degrees")
dc = input("enter if wave has a D.C value")

f = np.float16(f)  
k = np.float16(np.pi)

phi_rad = (phi_deg*k)/180   #changing phase shift in degrees to radians
tp = 1/f                    #time period of wave

t = np.linspace((-5*tp),5*tp,250) #taking samples
y = dc+np.sin((2*k*f*t)+phi_rad)
y1 = np.fft.fft(y)


plt.figure(1)
plt.plot(t,y)
plt.title("sine wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()


plt.figure(2)
plt.plot(y1)
plt.show()
