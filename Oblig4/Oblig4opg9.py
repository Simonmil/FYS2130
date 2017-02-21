import numpy as np
import pylab as plt

Fs = 1000. #Samplingsfrekvens
delta_t = 1./Fs # Tid mellom hver sampling
N = 1024 # Antall samplinger
t = np.linspace(0,N-1,Fs) # Tidsvektor


freqs = [100.0,200.0,400.0,700.0,950.0,1300.0] # Frekvens i hertz

for freq in freqs:

	x = 0.8*np.cos(2*np.pi*freq*t) # Signal en enkel cosinus

	plt.plot(Fs*t,x) # Plotting av signalet i tidsbildet
	plt.title("Opprinnelig signal i tidsbildet")
	plt.xlabel("tid/ms")
	plt.ylabel("Utslag")

	X = np.fft.fft(x,N)/N # Fouriertrans

	frekv = (Fs/2.)*np.linspace(0,1,N/2) # Frekvensvektor (for plot)

	plt.figure()

	plt.plot(frekv,2*np.abs(X[0:N/2.]))
	plt.title("Absolutt-verdier av frekvensspekteret")
	plt.xlabel("Frekvens/Hz")
	plt.ylabel("|X(frekv)|")

	plt.show()