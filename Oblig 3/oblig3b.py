import numpy as np
import pylab as plt


def a(v,z,b):
	m = 0.1 #kg
	k = 10. #N/m

	return -b/m*v - k/m*z

def RK4(N,dt,v,z,a,j):


	for i in range(0,int(N)-1):
		a1 = a(v[i],z[i],j)

		v2 = v[i] + a1*dt/2.0
		a2 = a(v2,z[i] + v[i]*dt/2.0,j)

		v3 = v[i] + a2*dt/2.0
		a3 = a(v3,z[i] + v2*dt/2.0,j)

		v4 = v[i] + a3*dt
		a4 = a(v4,z[i] + v3*dt,j)

		aMid = 1.0/6*(a1 + 2*a2 + 2*a3 + a4)
		vMid = 1.0/6*(v[i] + 2*v2 + 2*v3 + v4)

		z[i+1] = z[i] + vMid*dt
		v[i+1] = v[i] + aMid*dt


	return v,z


T = 2
dt = 0.0001
N = float(T)/dt
t = np.linspace(0,T,int(N))

b = [5.0,2.0,0.5] #kg/s


for j in b:

	v = np.zeros((int(N),2))
	z = np.zeros((int(N),2))
	z[0,1] = 0.1 #m

	v,z = RK4(N,dt,v,z,a,j)
	plt.plot(t,z[:,1])
	plt.title("Exercise b)")
	plt.xlabel("Time/s")
	plt.ylabel("Position/m")
plt.show()
