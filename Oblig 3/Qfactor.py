import numpy as np
import pylab as plt


def a(v,z,t,b,m,k,F,omega0):
	return -b/m*v - k/m*z + F/m*np.cos(omega0*t)

def RK4(N,dt,v,z,a,t,b,m,k,F,omega0):

	E = np.zeros(N)

	for i in range(0,int(N)-1):
		k = 10.
		m = 0.1
		a1 = a(v[i],z[i],t[i],b,m,k,F,omega0)

		v2 = v[i] + a1*dt/2.0
		a2 = a(v2,z[i] + v[i]*dt/2.0,t[i],b,m,k,F,omega0)

		v3 = v[i] + a2*dt/2.0
		a3 = a(v3,z[i] + v2*dt/2.0,t[i],b,m,k,F,omega0)

		v4 = v[i] + a3*dt
		a4 = a(v4,z[i] + v3*dt,t[i],b,m,k,F,omega0)

		aMid = 1.0/6*(a1 + 2*a2 + 2*a3 + a4)
		vMid = 1.0/6*(v[i] + 2*v2 + 2*v3 + v4)

		z[i+1] = z[i] + vMid*dt
		v[i+1] = v[i] + aMid*dt

		#if t[i] == 30:
		E[i] = 0.5*m*v[i,1]**2 + 0.5*k*z[i,1]**2



	return max(E)

T = 50
dt = 0.001
N = float(T)/dt
t = np.linspace(0,T,int(N))

v = np.zeros((int(N),2))
z = np.zeros((int(N),2))

m = 0.1 #kg
k = 10. #N/m
b = 0.040 #kg/s
F = 0.10 #N
omega0 = np.linspace(5,15,100)
E = np.zeros(len(omega0))

for i in omega0:
	E[np.where(omega0==i)] = RK4(N,dt,v,z,a,t,b,m,k,F,i)

f0 = omega0/(2*np.pi)
"""
plt.plot(f0,E)
plt.xlabel("Frequenzy/Hz")
plt.ylabel("Energy/J")
plt.title("Maximum energy for the frequencies")
plt.show()
"""
Emax = max(E)
f_fwhm = []
eps = 1e-2
for i in f0:
	f = np.where(f0==i)
	if Emax/2. - eps <= E[f] <= Emax/2. + eps:
		f_fwhm.append(i)
print f_fwhm

Delta_f = f_fwhm[1] - f_fwhm[0]

Q1 = m*omega0/b
Q2 = f0/Delta_f
plt.plot(f0,Q1)
plt.plot(f0,Q2)
plt.show()
