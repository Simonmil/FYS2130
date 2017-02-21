import numpy as np
import pylab as plt

Fs = 1000.
delta_t = 1./Fs
N = 512.
t = np.linspace(0,N,Fs)

f = [13./N,13.2/N]

for f in f:

	x = np.sin(2*np.pi*f*t)

	plt.plot(Fs*t,x)
	plt.title("Opprinnelig signal i tidsbildet")
	plt.xlabel("tid/ms")
	plt.ylabel("Utslag")

	X = np.fft.fft(x,int(N))/N

	frekv = (Fs/2.)*np.linspace(0,1,N/2.)

	plt.figure()

	plt.plot(frekv,2*np.abs(X[0:N/2.]))
	plt.title("Absolutt-verdier av frekvensspekteret")
	plt.xlabel("Frekvens/Hz")
	plt.ylabel("|X(frekv)|")

	plt.show()

