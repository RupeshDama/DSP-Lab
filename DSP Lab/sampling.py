#02.02.2019
# to record sound --- arecord -d time -r rate >filename.format

import scipy.io.wavfile as w
import numpy as np
import matplotlib.pyplot as plt

fs,data = w.read('eee_48000.wav')
k  = len(data)
t = np.linspace(0,k/fs,k)
plt.figure(1)
plt.plot(t,data)
plt.xlabel("-----> time in sec")
plt.ylabel("-----> amplitude")
plt.show()

