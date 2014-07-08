from obspy.core import read
from obspy.signal.filter import envelope
import matplotlib.pyplot as plt
import numpy as np

st = read('http://examples.obspy.org/COP.BHZ.DK.2009.050')
tr = st[0]

tr.trim(starttime=tr.stats.starttime, endtime=tr.stats.starttime+60*4)
tr.filter('lowpass', freq=.2)
env = envelope(tr.data)

t = np.linspace(0, 1, len(env))

fig = plt.figure()
ax = fig.gca()

ax.plot(t, tr.data, alpha=.6, color='k', lw=.75)

ax.set_title('')
ax.plot(t, env, linestyle='-', color='k', label='Envelope')
#ax.legend(loc=1)
ax.set_xticklabels('')
ax.set_yticklabels('')

ax.set_xlabel('Zeit')
ax.set_ylabel('Amplitude')

fig.set_size_inches(10, 3)
fig.savefig('../envelope.png', dpi=150)