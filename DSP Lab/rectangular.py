import numpy as np
import matplotlib.pyplot as plt
import dtft

M = input("filter length")
m = np.arange(0,M,1)
w_hm = np.ones(shape=(M,))
           
dw_hm = dtft.disctft(w_hm)
k = max(dw_hm)
dw_hm = dw_hm/k #normalisation
w = np.linspace(-3.143,3.143,1000)
mag = 20*np.log10(np.abs(dw_hm))
plt.title("Frequency response in dB Rectangular window of length 31")
plt.figure(1)
plt.plot(w,mag)
plt.xlabel('frequency')
plt.ylabel('magnitude in db')
plt.figure(2)
plt.title("Rectangular window of length 31")
plt.plot(m,w_hm)
plt.xlabel("-------> n")
plt.ylabel("magnitude of window")

plt.show()

