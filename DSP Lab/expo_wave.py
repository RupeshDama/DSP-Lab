import numpy as np
import matplotlib.pyplot as plt

a = input("scaling factor")
tk = np.linspace(0,10,1000)
#print tk
ye = np.exp2(a*tk)

#print ye
plt.plot(tk,ye)
plt.show()
