import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()


A = [.5, 2., 1., 1.5, .25]

dt = .5
wny = 2*np.pi*(1./dt)/2
t = np.linspace(-dt, len(A)*dt+dt, 300)

def sinc_interp(A, n):
	return A * np.sinc(wny*(t-dt*n))

sum_sinc = np.zeros_like(t)
for i, a in enumerate(A):
	this_sinc = sinc_interp(a, i)
	ax.plot(t, this_sinc, linewidth=.75, alpha=.7)
	sum_sinc += this_sinc

ax.plot(t, sum_sinc, color='k', linewidth=1.5, linestyle='dotted', label='Summe Sinc-Fkt.')

At = np.arange(0, len(A)) * dt
ax.plot(At, A, linewidth=1.5, linestyle='--', label='Originales Signal', marker='o', color='k')

ax.grid(alpha=.6)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.legend(fontsize=11)
#ax.set_title('Interpolation im Zeitbereich durch\nueberlagernde Sinc Funktionen', fontsize=11)
fig.set_size_inches(10, 4.5)
fig.savefig('interpolation_sinc.png', dpi=150)