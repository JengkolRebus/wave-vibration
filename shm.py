import matplotlib
import matplotlib.pyplot as plt
import numpy as np

B = 1           #Amplitudo
omega = np.pi   #sebesar pi()
t = np.arange(0.0, 20, 0.01)
s = B * np.sin(omega * t)

fig, ax = plt.subplots()
ax.plot(t,s)

ax.set(xlabel='waktu (s)', ylabel='Amplitudo', 
title='Grafik x = B sin(omega*t); omega=pi(), 0 <= t <= 20')
ax.grid()
plt.show()