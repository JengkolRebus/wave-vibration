# _jengkolrebus
# Curup, Bengkulu
# Mei 2019

import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.5, 0.01)
G = 1       #Amplitudo
r = (20, 25, 30)
m = 2
s = 2

fig, ax = plt.subplots()

for i in r:
    p = (-i*t)/(2*m)
    q = (np.square(i)/(4*np.square(m)))-(s/m)
    x = G * np.exp (p) * np.sinh(np.sqrt(q)) * t
    leg = 'r = ' + str(i)
    ax.plot(t, x, label=leg)
    ax.legend()

ax.set(xlabel='t', ylabel='x', 
        title='$x=G e^{-rt/2m} \sinh\left({\\frac{r^2}{4m^2}-\\frac{s}{m}}\\right)^{\\frac{1}{2}}t$' 
                '\n'
                '$G=1, s=2, m=2$')
ax.grid()
plt.show()