import numpy as np
import matplotlib.pylab as plt

# Konstanter
N = 8192
f1 = 1000.0; f2 = 1600.0 # Hz
c1 = 1.0; c2 = 1.7
fs = 10000.0 # Hz
T = N/fs
t = np.linspace(0,T,N)


# Genererer signal
x1 = 2*np.pi*f1*t; x2 = 2*np.pi*f2*t
f = c1*np.sin(x1) + c2*np.cos(x2)

# Plott
plt.subplot(1,2,1)
plt.plot(t[0:400],f[0:400])
plt.xlabel('Tid[s]',fontsize=20);plt.ylabel('f(t)', fontsize=20)
plt.title('Tidsbilde',fontsize=23)


# Fourier transform
F = np.fft.fft(f)
k = np.arange(N)
freq = k/T
freq = np.linspace(0,fs*(N-1)/float(N), N)

# Plott
plt.subplot(1,2,2)
plt.plot(freq[0:N/2.],(abs(F[0:N/2.])))
plt.xlabel('Frekvens [Hz]',fontsize=20);plt.ylabel('|F(t)|', fontsize=20)
plt.xlim([0.0,2000])
plt.title('Frekvensbilde',fontsize=23)
plt.tight_layout()
plt.show()

Kverdi = [24., 200.]

for K in Kverdi:
	fmax = 2000.
	fmin = 800.
	M = int(np.log(fmax/fmin) / np.log(1+(1./(8*K)))) + 1
	ftrinn = (fmax/fmin)**(1./(M-1))
	w_a = fmin
	T = float(N)/fs
	t = np.linspace(0,T*(N-1),N)
	w = np.linspace(0,fs*(N-1)/float(N),N)

	WL = np.zeros((M,N))
	wbrukt = np.zeros(M)

	for j in range(M):
		k = (K/w_a)**2
		FTwl = np.exp(-k*((w-w_a)**2))
		FTwl = FTwl - np.exp(-(K**2))*np.exp(-k*f*f)
		FTwl = 2.0*FTwl

		WL[j,:] = np.sqrt(abs(np.fft.ifft(FTwl*np.transpose(F))))

		wbrukt[j] = w_a
		w_a = w_a*ftrinn


	P = int((K*fs)/(24.*fmax))
	NP = int(float(N)/P)

	WL2 = np.zeros((M,NP))
	tP = np.zeros(NP)

	for j in range(M):
		for i in range(NP):
			WL2[j,i] = WL[j,i*P]
			tP[i] = t[i*P]

	plt.imshow(WL2, aspect='auto', origin='lower')
	plt.ylabel('Frekvens [Hz])',fontsize=20)
	plt.xlabel('Tid [s]',fontsize=20)
	plt.title('Waveletanalyse K = %.f'% K,fontsize=23)
	plt.colorbar()
	plt.savefig('ck%.f.png'% K)

	plt.tight_layout()
	plt.show()