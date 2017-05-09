import numpy as np
import pylab as plt
from matplotlib.animation import ArtistAnimation

N = 400. # masspoints
m = np.zeros(N)
m[1:200] = 0.02 # kg
m[200:399] = 0.06 # kg
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


anim = []
for t in range(4000):
	for i in range(1,int(N)-1):
		y_pluss[i] = (dt**2*(-(k[i-1] + k[i])*y_0[i] + k[i-1]*y_0[i-1] + k[i]*y_0[i+1]))/m[i] + 2*y_0[i] - y_minus[i]
	anim.append(plt.plot(y_0,'-b'))
	y_minus = np.copy(y_0)
	y_0 = np.copy(y_pluss)


fig = plt.figure(1)
plot = ArtistAnimation(fig,anim,interval=25)
plt.show()