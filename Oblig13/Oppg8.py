import numpy as np 
import pylab as plt



Fs = 10000. # Hz
N = 8192.
f1 = 1000. # Hz
f2 = 1600. # Hz
c1 = 1.0
c2 = 1.7

t = np.linspace(0,N-1,Fs)

f = c1*np.sin(2*np.pi*f1*t) + c2*np.cos(2*np.pi*f2*t)

plt.plot(t[0:400],f[0:400])
plt.xlabel('Time/s')
plt.ylabel('Amplitude')
plt.title(r'a) Plott av funksjonen $f = c_1\sin(2\pi*f_1t) + c_2\cos(2\pi*f_2t)$')

fft = np.fft.fft(f,int(N))/N

frekv = (Fs/2.)*np.linspace(0,1,N/2)

plt.figure()

plt.plot(frekv,2*np.abs(fft[0:N/2.]))
plt.xlabel('Frekvens/Hz')
plt.ylabel('|fft(frekv)|')
plt.title('Absolutt-verdier av frekvensspekteret')
plt.show()


