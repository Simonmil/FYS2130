import numpy as np
import pylab as plt
from scipy import signal



Fs = 10000. # Hz
N = 8192.
f1 = 1000 # Hz
f2 = 1600 # Hz
c1 = 1.0
c2 = 1.7

fmin = 800. # Hz
fmax = 1200. # Hz

K = [24.,200.]

T = N/Fs
#t = np.linspace(0,T*(N-1)/int(N),N)
t = np.linspace(0,N-1,Fs)
f = c1*np.sin(2*np.pi*f1*t) + c2*np.sin(2*np.pi*f2*t)
FTsig = np.fft.fft(f,int(N))/N


widths = np.arange(1,31)
cwtmatr = signal.cwt(FTsig,signal.ricker,widths)

plt.imshow(cwtmatr,extent=[-1,1,1,31],cmap='PRGn',aspect='auto',vmax=np.abs(cwtmatr).max(),vmin = -np.abs(cwtmatr).max())
plt.show()
