import numpy as np
import pylab as plt

times = []
sunspots = []
fin = open("SN_y_tot_V2.0.txt","r")

for line in fin:
	cols = line.split()
	times.append(float(cols[0]))
	sunspots.append(float(cols[1]))
fin.close()

times = np.array(times)
sunspots = np.array(sunspots)

plt.plot(times,sunspots,"-b")
plt.xlabel("Tid")
plt.ylabel("Solflekker")

X = np.fft.fft(sunspots)/(len(sunspots))
frekv = np.linspace(0,1,len(sunspots)/2)
#frekv = 1./times


plt.figure()

plt.plot(frekv[0:len(times)/2.],2*np.abs(X[0:len(sunspots)/2.]))


plt.show()