import numpy as np
import pylab as plt


def a(v,z,t,c,b,m,k,F,omega0):
	return -b/m*v - k/m*z + F/m*np.cos(c*omega0*t)

def RK4(N,dt,v,z,a,t,c,b,m,k,F,omega0):


	E = []
	for i in range(0,int(N)-1):
		k = 10.
		m = 0.1
		a1 = a(v[i],z[i],t[i],c,b,m,k,F,omega0)

		v2 = v[i] + a1*dt/2.0
		a2 = a(v2,z[i] + v[i]*dt/2.0,t[i],c,b,m,k,F,omega0)

		v3 = v[i] + a2*dt/2.0
		a3 = a(v3,z[i] + v2*dt/2.0,t[i],c,b,m,k,F,omega0)

		v4 = v[i] + a3*dt
		a4 = a(v4,z[i] + v3*dt,t[i],c,b,m,k,F,omega0)

		aMid = 1.0/6*(a1 + 2*a2 + 2*a3 + a4)
		vMid = 1.0/6*(v[i] + 2*v2 + 2*v3 + v4)

		z[i+1] = z[i] + vMid*dt
		v[i+1] = v[i] + aMid*dt

		#if t[i] == 30:
		e = 0.5*m*v[i,1]**2 + 0.5*k*z[i,1]**2
		E.append(e)



	return v,z,E

T = 50
dt = 0.001
N = float(T)/dt
t = np.linspace(0,T,int(N))

v = np.zeros((int(N),2))
z = np.zeros((int(N),2))

con = [1.0,0.9]

m = 0.1 #kg
k = 10. #N/m
b = 0.040 #kg/s
F = 0.10 #N
omega0 = np.sqrt(k/m)

for c in con:
	v,z,E = RK4(N,dt,v,z,a,t,c,b,m,k,F,omega0)
	plt.figure(con.index(c)+1)
	plt.plot(t,z[:,1])

plt.show()

omega = np.linspace(5,50,250)
Emax = []
for omega in omega:
	c = 1
	v,z,E = RK4(N,dt,v,z,a,t,c,b,m,k,F,omega)
	Emax.append(np.max(E))
f = omega/(2*np.pi)
plt.plot(f,Emax)
plt.show()
