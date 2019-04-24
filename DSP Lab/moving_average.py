import numpy as np
import scipy.io.wavfile as w
import matplotlib.pyplot as plt

fs,data = w.read('tuning_fork.wav')
k = len(data)
data = np.asarray(data)
n = np.random.uniform(-20000,20000,(k,2))
d_n = data+n
r = np.zeros((k,2),dtype=float)
for h in range(2):
	for i in range(k):
		s=0
		for j in range(k):
			if(i+j < k):
				s = s+d_n[i+j,h]
		r[i,h] = s/k

plt.plot(r)
plt.show()
