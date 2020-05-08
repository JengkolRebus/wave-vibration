# _jengkolrebus
# Curup, Bengkulu
# Mei 2020

import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 15, 0.01)
A = 1           #Amplitudo
r = 0.5
m = 0.5
s = 30.0
phi = (1)*np.pi

p = (-r*t)/(2*m)
q = (s/m)-(np.square(r)/(4*np.square(m)))

omega = np.sqrt(q)
x = A*np.exp(p)*np.sin((omega*t)+phi)

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set(xlabel='t', ylabel='x', 
        title='$x=A e^{-rt/2m} \sin(\omega^\prime t + \phi)$' '\n'
                '$A=1, r=0.5, s=30, m=0.5, \phi = \pi$')
# ax.set_title('$x=A e^{-rt/2m} \sin(\omega^\prime t + \phi)$' '\n'
#                 '$A=1, r=0.5, s=30, m=0.5, \phi = \pi$')
ax.grid()
plt.show()