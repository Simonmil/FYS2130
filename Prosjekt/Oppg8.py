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
#maxt = ((N/3.5)*np.sqrt(m[1]/k[1])*10)/dt
vB = np.sqrt(k[1]/m[1])

y_0 = np.zeros(N)
y_minus = np.zeros(N)
y_pluss = np.zeros(N)

for i in range(int(N)):
	if 1 <= i <= 30:
		y_0[i] = i/30.
	elif 31 <= i <= 60:
		y_0[i] = (60. - i)/30.
	else:
		y_0[i] = 0


for i in range(int(N)):
	if 0 <= i <= 29:
		y_minus[i] = y_0[i] + 1/30.*dt*vB
	elif 30 <= i <= 59:
		y_minus[i] = y_0[i] - 1/30.*dt*vB
	else:
		y_0[i] = y_0[i]

all_pos = []
anim = []
for t in range(4000):
	for i in range(1,int(N)-1):
		y_pluss[i] = (dt**2*(-(k[i-1] + k[i])*y_0[i] + k[i-1]*y_0[i-1] + k[i]*y_0[i+1]))/m[i] + 2*y_0[i] - y_minus[i]
	anim.append(plt.plot(y_0,'-b'))
	y_minus = np.copy(y_0)
	y_0 = np.copy(y_pluss)
	all_pos.append(y_0)

plt.figure(2)
plt.plot(all_pos[0], label=r'$t_{step} = 0$')
plt.plot(all_pos[500], label=r'$t_{step} = 500$')
plt.plot(all_pos[1000], label=r'$t_{step} = 1000$')
plt.plot(all_pos[2500], label=r'$t_{step} = 2500$')
plt.plot(all_pos[3200], label=r'$t_{step} = 3200$')
plt.xlabel('Position on the string')
plt.ylabel('Amplitude')
plt.legend()

fig = plt.figure(1)
plot = ArtistAnimation(fig,anim,interval=25)
plt.show()