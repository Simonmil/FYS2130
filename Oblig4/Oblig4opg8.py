import numpy as np

Fs = 1000.
delta_t = 1./Fs
N = 1024
t = np.linspace(0,N-1,Fs)


f = 100.0
x = np.sin(2*np.pi*f*t)

X = np.fft.fft(x,1)

print X