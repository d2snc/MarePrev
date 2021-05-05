import ttide as tt
import numpy as np
import matplotlib.pyplot as plot
import math

t = np.arange(1001) #t é um vetor que vai de 0 até 1000
m2_freq = 2 * np.pi / 12.42

elev = 5 * np.cos(m2_freq * t)


tfit_e = tt.t_tide(elev)

t = np.arange(0, 20, 0.2);

amplitude = np.cos(28.984*t-127.24)*0.0004 + np.cos(30*t-343.66)*0.538
plot.plot(t, amplitude)
plot.title('Cosine wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = cosine(time)')
#plot.grid(True, which='both')
plot.axhline(y=0, color='b')
plot.show()

