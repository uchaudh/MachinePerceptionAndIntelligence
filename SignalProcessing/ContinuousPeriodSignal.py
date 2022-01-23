#!/usr/bin/env python3

import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt

# initialize time and sampling frequency
t0 = 0
tf = 0.1
f = 1*10**3		        # 1 KHz sampling frequency
step = 1/f 		        # Time spacing (s)		
t = np.arange(t0,tf,step)

# Continuous period signal
x = 2 + 3*cos(500*pi*t) + 2*cos(1000*pi*t) + 3*sin(2000*pi*t)

#Fast Fourier Transform of x, plot in freqeuncy domain
x_fft = abs(np.fft.fft(x))
freq = abs(np.fft.fftfreq(len(t), d = step))

# plot x in the time domain
plt.figure()
plt.plot(t,x)
plt.title('Continuous Signal in time domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plot x in the frequency domain
plt.figure()
plt.plot(freq,x_fft)
plt.title('Fast Fourier Transform of Continuous Signal ')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.show()
