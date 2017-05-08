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

y_0 = np.zeros(N)
y_minus = np.zeros(N)
y_pluss = np.zeros(N)

for i in range(70,100,1):
	y_0[i] = (i-69.)/30. 
	y_minus[i] = (i-69.)/30.

for i in range(100,129,1):
	y_0[i] = (129-i)/30. 
	y_minus[i] = (129-i)/30. 

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