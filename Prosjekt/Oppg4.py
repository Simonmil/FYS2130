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
time = np.linspace(0,1200,N)
dt = np.sqrt(m[1]/k[0])*1e-1



y_0 = np.array([np.sin(7*np.pi*i/(N-1)) for i in range(int(N))])
y_minus = np.array([np.sin(7*np.pi*i/(N-1)) for i in range(int(N))])

y_pluss = np.zeros(N)

all_pos = []
anim = []

for t in range(1200):
	for i in range(1,int(N)-1):
		y_pluss[i] = (dt**2*(-(k[i-1] + k[i])*y_0[i] + k[i-1]*y_0[i-1] + k[i]*y_0[i+1]))/m[i] + 2*y_0[i] - y_minus[i]
	anim.append(plt.plot(y_0,'-b'))
	y_minus = np.copy(y_0)
	y_0 = np.copy(y_pluss)
	all_pos.append(y_0)


plt.figure(2)
plt.plot(all_pos[0], label='Pos at t-step = 0')
plt.plot(all_pos[80], label='Pos at t-step = 80')
plt.plot(all_pos[150], label='Pos at t-step = 150')
plt.xlabel("Length of string")
plt.ylabel("Amplitude")
plt.legend()
plt.title('Position of different timesteps for a standing sinewave.')


fig = plt.figure(1)
plot = ArtistAnimation(fig,anim,interval=25)
plt.show()

