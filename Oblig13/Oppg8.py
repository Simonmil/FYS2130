import numpy as np 
import pylab as plt



Fs = 10000.0 # Hz
N = 8192
f1 = 1000.0 # Hz
f2 = 1600.0 # Hz
c1 = 1.0
c2 = 1.7
T = N/Fs
t = np.linspace(0,T,N)

f = c1*np.sin(2*np.pi*f1*t) + c2*np.cos(2*np.pi*f2*t)

plt.plot(t[0:500],f[0:500])
plt.xlabel('Tid [s]')
plt.ylabel('Amplitude')
plt.title(r'a) Plott av funksjonen $f = c_1\sin(2\pi*f_1t) + c_2\cos(2\pi*f_2t)$')

fft = np.fft.fft(f)
k = np.arange(N)
frekv = k/T
frekv = np.linspace(0,Fs*(N-1)/float(N),N)

plt.figure()

plt.plot(frekv[0:N/2.],abs(fft[0:N/2.]))
plt.xlabel('Frekvens [Hz]')
plt.ylabel('|fft(frekv)|')
plt.xlim([0.0,2000])
plt.title('Absolutt-verdier av frekvensspekteret')
plt.show()


