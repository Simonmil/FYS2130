import numpy as np
import pylab as plt





N = 200. # masspoints
m = np.zeros(N)
m[1:N-1] = 0.02 # kg
print m
k = 10. # kg/s2

#for t in range
for i in range(1,N-2):
	y_0[i] = np.sin(7*np.pi*(i/(N-1)))

