#date = 18/03/2019
#filters using windows techniques
#Released under GNU 2.0 Lesser public license
import numpy as np 
import matplotlib.pyplot as plt

#dtft function
def disctft(a):
	a = np.asarray(a)
	l_aa = a.shape
	l_a = l_aa[0]
	print l_a
	p = np.pi
	w = np.linspace(-3.143j,3.143j,1000)
	l=1000
	y = np.zeros((l),dtype = complex)
	for k in range(l):
		s = 0
		for m in range(l_a):
			s = s+(a[m]*(np.exp(-(m*w[k]))))
		y[k]=s
	return y

rng = np.arange(-100,100,1)
p = np.pi
h = 0.25*(np.sinc(rng*0.25))
d_h = disctft(h)
d_h = np.abs(d_h)
w = np.linspace(-3.143,3.143,1000)
plt.figure(1)
plt.subplot(3,2,1)
plt.stem(w,d_h)

#windows generation
#rectangular windom

m = input("window length")
mn = np.arange(0,m,1)
wr = np.ones(m)
print wr

#triangular window

wt = np.empty(m)
for i in range(m):
	k1 = np.abs(2*(i-((m-1)/2)))
	k1 = float(k1)
	wt[i] = 1-(k1/(m-1))
	
plt.subplot(3,2,2)
plt.stem(wt)

#hanning window
m_f = float(m)

whn = 0.5-(0.5*(np.cos(2*p*mn/(m_f-1))))
plt.subplot(3,2,3)
plt.stem(whn)

#hamming wndow

whm = 0.54-(0.46*(np.cos(2*p*mn/(m_f-1))))
plt.subplot(3,2,4)
plt.stem(whm)

#blackman window
wbm = 0.42-(0.5*(np.cos(2*p*mn/(m_f-1))))+(0.08*(np.cos(4*p*mn/(m_f-1))))
plt.subplot(3,2,5)
plt.stem(wbm)

#filtering and plotting frequency response
hp = h[100:(100+m)]
#rectangular 
fr = hp*wr
dfr = disctft(fr)
plt.figure(2)
plt.subplot(3,2,1)
plt.plot(w,dfr)
plt.ylabel("rectangular")

#triangular window
ft = hp*wt
d_ft = disctft(ft)
plt.subplot(3,2,2)
plt.plot(w,d_ft)
plt.ylabel("triangular")

#hanning window
fhn = hp*whn
dfhn = disctft(fhn)
plt.subplot(3,2,3)
plt.plot(w,dfhn)
plt.ylabel("hanning")

#hamming window
fhm = hp*whm
dfhm = disctft(fhm)
plt.subplot(3,2,4)
plt.plot(w,dfhm)
plt.ylabel("hamming")

#blackman window
fbm = hp*wbm
dfbm = disctft(fbm)
plt.subplot(3,2,5)
plt.plot(w,dfbm)
plt.ylabel("blackman")
plt.show()
