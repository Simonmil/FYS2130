import numpy as np
import pylab as plt


def a(v,z,t):
	m = 0.1 #kg
	k = 10. #N/m
	b = 0.040 #kg/s
	F = 0.10 #N

	return -b/m*v - k/m*z + F/m*np.cos(0.9*omega0*t)

def RK4(N,dt,v,z,a,t):


	for i in range(0,int(N)-1):
		a1 = a(v[i],z[i],t[i])

		v2 = v[i] + a1*dt/2.0
		a2 = a(v2,z[i] + v[i]*dt/2.0,t[i])

		v3 = v[i] + a2*dt/2.0
		a3 = a(v3,z[i] + v2*dt/2.0,t[i])

		v4 = v[i] + a3*dt
		a4 = a(v4,z[i] + v3*dt,t[i])

		aMid = 1.0/6*(a1 + 2*a2 + 2*a3 + a4)
		vMid = 1.0/6*(v[i] + 2*v2 + 2*v3 + v4)

		z[i+1] = z[i] + vMid*dt
		v[i+1] = v[i] + aMid*dt

	return v,z


T = 50
dt = 0.0001
N = float(T)/dt
t = np.linspace(0,T,int(N))


v = np.zeros((int(N),2))
z = np.zeros((int(N),2))

m = 0.1 #kg
k = 10. #N/m
b = 0.040 #kg/s


for c in con:
	v,z = RK4(N,dt,v,z,a,t)



plt.plot(t,z[:,1])
plt.show()