import numpy as np
import pylab as plt
from matplotlib.animation import ArtistAnimation

N = 200. # masspoints
m = np.zeros(N)
m[1:N-1] = 0.02 # kg
m[0] = 100000. # kg
m[-1] = m[0]
k = np.zeros(N-1)
k[:] = 10. # kg/s2
dt = np.sqrt(m[1]/k[0])*1e-1
maxt = 5714
#maxt = ((N/3.5)*np.sqrt(m[1]/k[1])*10)/dt

y_0 = np.array([np.sin(7*np.pi*i/(N-1)) for i in range(int(N))])
y_minus = np.array([np.sin(7*np.pi*i/(N-1)) for i in range(int(N))])

y_pluss = np.zeros(N)

pos99 = []
anim = []

count = 0

for t in range(int(maxt)):
	for i in range(1,int(N)-1):
		y_pluss[i] = (dt**2*(-(k[i-1] + k[i])*y_0[i] + k[i-1]*y_0[i-1]\
		 + k[i]*y_0[i+1]))/m[i] + 2*y_0[i] - y_minus[i]
		if i == 99:
			pos99.append(y_pluss[i])
			if y_pluss[i] > 0 and y_0[i] < 0:
				count += 1
			"""
			elif y_pluss[i] < 0 and y_0[i] > 0:
				count += 1
			"""
	y_minus = np.copy(y_0)
	y_0 = np.copy(y_pluss)

numfreq = count/(dt*maxt)
print numfreq

plt.figure(1)
plt.plot(pos99)
plt.xlabel('Position on the string')
plt.ylabel('Amplitude')
plt.title('The movement of position 100 as time progresses')
plt.show()

FFtpos99 = np.fft.fft(pos99)/(len(pos99))
frekv = np.linspace(0,1,len(pos99))


plt.figure(2)
plt.plot(frekv,abs(FFtpos99)**2)
plt.xlabel('Frequency')
plt.ylabel(r'$|FFT(position99)|^2$')
plt.title('The Fourier Transform of the position of element 100.')

plt.show()