import numpy as np
import pylab as plt

#Position array
x = np.linspace(-20,20,400)
n = len(x)

#Initial positions
sigma = 2.0
u = np.exp(-(x/(2*sigma))*(x/(2*sigma)))
plt.plot(x,u,'-r')
plt.figure(1)
plt.show()

# Generates div parameters and timederivatives of the amp at t=0
v = 0.5
delta_t = 0.1
delta_x = 0.1
factor = (delta_t*v/delta_x)**2
dudt = (v/(2*sigma*sigma))*x*u

# Gives effective initial conditions

u_jminus1 = u - delta_t*dudt
u_j = u

u_jplus1 = np.zeros(400)

for i in range(len(x)):
	if i == 0:
		u_jplus1[i] = (2*(1-factor))*u_j[i] - u_jminus1[i] + factor*(u_j[i+1])
	elif i == n-1:
		u_jplus1[i] = (2*(1-factor))*u_j[i] - u_jminus1[i] + factor*(u_j[i-1])
	else:
		u_jplus1[i] = (2*(1-factor))*u_j[i] - u_jminus1[i] + factor*(u_j[i+1]) + u_j[i-1]

	plt.plot(u_j)
	plt.xlim([0,n+1])
	plt.ylim([-0.3,1.2])

	u_jminus1 = u_j
	u_j = u_jplus1
plt.show()
