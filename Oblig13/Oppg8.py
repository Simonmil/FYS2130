import numpy as np 
import pylab as plt



Fs = 10000. # Hz
N = 8192
f1 = 1000 # Hz
f2 = 1600 # Hz
c1 = 1.0
c2 = 1.7

t = np.linspace(0,N-1,Fs)

f = c1*np.sin(2*np.pi*f1*t) + c2*np.sin(2*np.pi*f2*t)

plt.plot(t[0:400],f[0:400])
plt.xlabel('Time/s')
plt.ylabel('Amplitude')
plt.title(r'Plot of the function $f = c_1\sin(2\pi*f_1t) + c_2\sin(2\pi*f_2t)$')
plt.show()





