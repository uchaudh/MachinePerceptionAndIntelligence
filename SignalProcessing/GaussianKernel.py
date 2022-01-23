#!/usr/bin/env python3

import numpy as np
from numpy import sqrt, exp, pi
import matplotlib.pyplot as plt

def convolution(noise, kernel):
	# establish length for empty convolution array
	C = np.zeros(len(noise) + len(kernel) - 1)
	for i in range(len(noise)):
		for j in range(len(kernel)):
			C[i+j] = C[i+j] + noise[i]*kernel[j]
	# reshape convolution array
	C = C[1:500]
	return C

# define variables for probability density function
mean = 0
var = 1
std = sqrt(var)

#define time domain
k = np.arange(0,499)

#define x(k) and n(k)
x = []
for i in range(len(k)):  
	x.append(20)

n = np.random.normal(mean, std, len(k))
xp = x + n
# gaussian kernels 
hk3 = [0.27901, 0.44198, 0.27901] 			
hk11 = [0.000003, 0.000229, 0.005977, 0.060598, 0.24173, 0.382925, 0.24173, 0.060598, 0.005977, 0.000229, 0.000003]
c3 = convolution(n,hk3)
c11 = convolution(n,hk11)

# calculate x'(k) = x(k) + gaussian smoothened noise
xp3 = x + c3
xp11 = x + c11

# a) Visualize both x(k) and xp(k) in one figure
plt.figure()
plt.plot(k,xp,k,x)
plt.title('x(k) and xp(k)')
plt.xlabel('k')
plt.ylabel('Amplitude')

# b) visualize both x(k) and y(k) in one figure with kernel size 3
plt.figure()
plt.plot(k,xp3,k,x)
plt.title('x(k) and y(k) with kernel window size 3')
plt.xlabel('sigma')
plt.ylabel('Amplitude')

# c) visualize both x(k) and y(k) in one figure with kernel size 11
plt.figure()
plt.plot(k,xp11,k,x)
plt.title('x(k) and y(k) with kernel window size 11')
plt.xlabel('sigma')
plt.ylabel('Amplitude')

plt.show()
