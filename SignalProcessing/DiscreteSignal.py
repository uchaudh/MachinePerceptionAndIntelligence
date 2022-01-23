#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def square(t0, tf): 
	# convert to microseconds to iterate loops in microseconds
	cf = 10**(-6)
	t_0 = t0
	t_f = tf
	# print(t_f)
	signal = []
	that = 0
	while t_0 <= t_f:
		k = 0
		while k < 1000*cf:
			if k <= 499*cf:
				signal.append(0) 
			elif k > 499*cf:
				signal.append(1)
			t_0 = t_0 + cf
			k = k + cf
	return signal

t0 = 0				# seconds
tf = 0.025			# seconds
f = 1*10**6		# 1 MHz sampling frequency			
step = 1/f 		# step size in seconds									
t = np.arange(t0,tf,step)
y = square(t0,tf)
time = np.arange(0,25000,1).tolist()

# compute fast Fourier Transform of x, plot in freqeuncy domain
y_fft = np.fft.fft(y)
freq = np.fft.fftfreq(len(y),d = step)

plt.figure()
plt.plot(time, y)
plt.title('Discrete Signal in ')
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')

plt.figure()
plt.plot(freq,y_fft)
plt.title('Frequency Domain of Discrete Signal ')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
