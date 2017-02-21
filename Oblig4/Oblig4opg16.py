import numpy as np
import pylab as plt
from scipy import signal

Fs = 1000.
delta_t = 1./Fs
N = 16384
t = np.linspace(0,N-1,Fs)
f = 16./N
x = signal.square(2*np.pi*f*t)

plt.plot(t, x)
plt.title("Opprinnelig signal i tidsbildet")
plt.xlabel("tid/ms")
plt.ylabel("Utslag")

plt.figure()

X = np.fft.fft(x,N)/N
frekv = (Fs/2.)*np.linspace(0,1,N/2.)

plt.plot(frekv,2*np.abs(X[0:N/2.]))
plt.title("Absolutt-verdier av frekvensspekteret")
plt.xlabel("Frekvens/Hz")
plt.ylabel("|X(frekv)|")

plt.show()
