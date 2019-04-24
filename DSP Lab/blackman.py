import numpy as np
import matplotlib.pyplot as plt
import dtft

M = input("filter length")
m = np.arange(0,M,1)
w_hm = 0.42-(0.5*(np.cos((2*np.pi*m)/(M-1))))+(0.08*(np.cos((4*np.pi*m)/(M-1))))
           
dw_hm = dtft.disctft(w_hm)
k = max(dw_hm)
dw_hm = dw_hm/k #normalisation
w = np.linspace(-3.143,3.143,1000)
mag = 20*np.log10(np.abs(dw_hm))
plt.title("Frequency response in dB Blackman window of length 31")
plt.figure(1)
plt.plot(w,mag)
plt.xlabel('frequency')
plt.ylabel('magnitude in db')
plt.figure(2)
plt.title("Blackman window of length 31")
plt.plot(m,w_hm)
plt.xlabel("-------> n")
plt.ylabel("magnitude of window")

plt.show()

