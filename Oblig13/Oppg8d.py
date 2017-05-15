import numpy as np
import pylab as plt
from scipy import signal



Fs = 10000. # Hz
N = 8192.
f1 = 1000 # Hz
f2 = 1600 # Hz
c1 = 1.0
c2 = 1.7
t1 = 0.15 # s
t2 = 0.5 # s
sigma1 = 0.01 # s
sigma2 = 0.1 # s

fmin = 800. # Hz
fmax = 1200. # Hz

K = [24.,200.]

T = N/Fs
#t = np.linspace(0,T*(N-1)/int(N),N)
t = np.linspace(0,N-1,Fs)
f = c1*np.sin(2*np.pi*f1*t)*np.exp(-((t-t1)/sigma1)**2) + c2*np.sin(2*np.pi*f2*t)*np.exp(-((t-t2)/sigma2)**2)
FTsig = np.fft.fft(f,int(N))/N

plt.plot(t,f)
plt.xlabel('Tid/s')
plt.ylabel('Utslag')
plt.title('Plot i tidsbildet')

frekv = (Fs/2.)*np.linspace(0,1,N/2)

plt.figure()
plt.plot(frekv, 2*np.abs(FTsig[0:N/2.]))
plt.xlabel('Frekvens/Hz')
plt.ylabel('|Fouriertransform|')
plt.title(r'Fouriertransform av $f = c_1\sin(2\pi f_1t)e^{-(t-t_1)/\sigma_1} + c_2\sin(2\pi f_2t)e^{-(t-t_2)/\sigma_2}$')

widths = np.arange(1,31)
cwtmatr = signal.cwt(FTsig,signal.ricker,widths)

plt.figure()
plt.imshow(cwtmatr,extent=[-1,1,1,31],cmap='hot',aspect='auto',vmax=np.abs(cwtmatr).max(),vmin = -np.abs(cwtmatr).max())
plt.show()