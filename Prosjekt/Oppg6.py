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
maxt = ((N/3.5)*np.sqrt(m[1]/k[1])*10)/dt

y_0 = np.array([np.sin(7*np.pi*i/(N-1)) for i in range(int(N))])
y_minus = np.array([np.sin(7*np.pi*i/(N-1)) for i in range(int(N))])
y_pluss = np.zeros(N)
#E_tot = np.zeros(N)

E_tot = 0

for t in range(int(maxt)):
	for i in range(1,int(N)-1):
		y_pluss[i] = (dt**2*(-(k[i-1] + k[i])*y_0[i] + k[i-1]*y_0[i-1] + k[i]*y_0[i+1]))/m[i] + 2*y_0[i] - y_minus[i]		
		E_tot += 0.5*m[i]*((y_pluss[i] - y_minus[i])/(2*dt))**2 + 0.5*k[i]*(y_0[i] - y_0[i-1])**2
	y_minus = np.copy(y_0)
	y_0 = np.copy(y_pluss)

print E_tot