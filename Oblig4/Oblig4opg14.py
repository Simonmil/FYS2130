import numpy as np
import pylab as plt

Fs = 1000.
delta_t = 1./Fs
N = 512.
t = np.linspace(0,N,Fs)

f = 13./N

x = np.sin(2*np.pi*f*t)

plt.plot(Fs*t,x)

X = np.fft.fft(x,int(N))/N

frekv = (Fs/2.)*np.linspace(0,1,N/2.)

plt.figure()

plt.plot(frekv,2*np.abs(X[0:N/2.]))
print f
plt.show()

