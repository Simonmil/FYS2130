import numpy as np
import pylab as plt
from scipy import signal

Fs = 1000.
delta_t = 1./Fs
N = 1024
t = np.linspace(0,N-1,16384)
f = 16./N
x = signal.square(2*np.pi*f*t)

plt.plot(t, x)

plt.figure()

X = np.fft.fft(x,N)/N
frekv = (Fs/2.)*np.linspace(0,1,N/2.)

plt.plot(frekv,2*np.abs(X[0:N/2.]))
plt.show()
