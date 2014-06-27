import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def boxcar(x, width=.7, amp=1.):
  bc = np.zeros_like(x)
  for i in xrange(bc.size):
    if i <= bc.size*(1.-width)/2 or i >= bc.size-(bc.size*(1-width)/2):
      continue
    else:
      bc[i] = amp
  return bc
  
  
def cdf(x):
  cd = np.empty_like(x)
  fac = np.sum(x)
  for i in xrange(x.size):
    cd[i] = np.sum(x[0:i]/fac)
  return cd

def simpleaxis(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.get_xaxis().tick_bottom()
  ax.get_yaxis().tick_left()

s = np.linspace(0, 10, 200)

# Wahrscheinlichkeitsdichtefunktionen
pdfs = []

pdfs.append(dict(
  pdf=stats.norm.pdf(s, loc=5),
  name='Gausssche Normalverteilung'))
  
pdfs.append(dict(
  pdf=stats.norm.pdf(s, loc=6, scale=1) +\
	  stats.norm.pdf(s, loc=3, scale=.5),
  name='Bimodale Dichteverteilung'))
  
pdfs.append(dict(
  pdf=boxcar(s, width=.6, amp=.2),
  name='Boxcar Dichteverteilung'))  
  	  
# Plotting
fig, axes = plt.subplots(len(pdfs), 2)
for i, pdf in enumerate(pdfs):
  ax = fig.axes[i*2]
  cax = fig.axes[i*2+1]
  ax.fill_between(s, pdf['pdf'], facecolor='gray', alpha=.8)
  ax.text(.025, .95, pdf['name'], transform=ax.transAxes, fontsize=9, alpha=.8)
  
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_ylim(0, 1.2*pdf['pdf'].max())
  
  cax.plot(s, cdf(pdf['pdf']), color='k', alpha=.8)
  
  cax.set_xticks([])
  cax.set_yticks([0, 1])
  cax.set_yticklabels([0, 1])
  simpleaxis(cax)
  simpleaxis(ax)
  
  if i == 0:
    cax.set_title('Wahrscheinlichkeitsverteilungen', fontsize=10)
    ax.set_title('Wahrscheinlichkeitsdichteverteilung', fontsize=10)
    
fig.set_size_inches(10, 10)  
fig.savefig('../dichtefunktionen.png', dpi=150)
