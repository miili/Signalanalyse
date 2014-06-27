import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.signal import correlate


def boxcar(x, width=.7, amp=1.):
  bc = np.zeros_like(x)
  for i in xrange(bc.size):
    if i <= bc.size*(1.-width)/2 or i >= bc.size-(bc.size*(1-width)/2):
      continue
    else:
      bc[i] = amp
  return bc
  
def simpleaxis(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.get_xaxis().tick_bottom()
  ax.get_yaxis().tick_left()

s = np.linspace(0, 10, 200)


# Plotting
fig, _ = plt.subplots(1,2)
ax = fig.axes[0]
akax = fig.axes[1]

bc = boxcar(s)

ax.fill_between(s, bc, facecolor='gray', alpha=.8)  
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim(0, 1.5*bc.max())
ax.set_xlabel('$t$')
ax.set_ylabel('$x(t)$')

akbc = correlate(bc, bc)
akax.fill_between(range(len(akbc)), akbc, facecolor='gray', alpha=.8)
akax.set_xticks([])
akax.set_yticks([])
#akax.set_ylim(0, 1.5*bc.max())
akax.set_xlabel('$t$')
akax.set_ylabel('$R_{xx}(t)$')

simpleaxis(akax)
simpleaxis(ax)
ax.text(.05, 1, 'a)', transform=ax.transAxes, fontsize=11, va='top')
akax.text(.05, 1, 'b)', transform=akax.transAxes, fontsize=11, va='top')

  
fig.set_size_inches(6, 2)  
fig.savefig('../01-example_boxcar.png', dpi=150)