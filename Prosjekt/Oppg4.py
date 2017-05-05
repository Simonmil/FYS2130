import numpy as np
import pylab as plt


N = 200. # masspoints
m = np.zeros(N)
m[1:N-1] = 0.02 # kg
m[0] = 100. # kg
m[-1] = m[0]
k = np.zeros(N-1)
k[:] = 10. # kg/s2
time = np.linspace(0,1200,N-1)
dt = np.sqrt(m[1]/k[0])*1e-3


y_0 = [np.sin(7*np.pi*i/(N-1)) for i in range(int(N)-1)]
init = y_0
y_0[0] = 0
y_0[-1] = y_0[0]
y_minus = np.zeros(N)
y_pluss = np.zeros(N)
all_pos = []


for t in range(len(time)):
	for i in range(1,int(N)-2):
		y_pluss[i] = (dt**2*(-(k[i-1] + k[i])*y_0[i] + k[i-1]*y_0[i-1] + k[i]*y_0[i+1]))/m[i] + 2*y_0[i] - y_minus[i]
		y_minus[i] = y_0[i]
		y_0[i] = y_pluss[i]
	all_pos.append(y_0)

for t in range(len(time)):
	plt.plot(init,all_pos[t])
	plt.show()
