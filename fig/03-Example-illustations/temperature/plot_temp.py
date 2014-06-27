import matplotlib.pyplot as plt
import numpy as np
from datetime import date

class meteo(object):
  def __init__(self, filename=None):
    if filename is not None:
      ddata = []
      temp = []
      
      with file(filename, 'r') as f:
	for line in f.xreadlines():
	  ddata.append(date(int(line[7:11]), int(line[11:13]), int(line[13:15])))
	  temp.append(int(line[43:47]))
      self.date = ddata
      self.temp = np.array(temp)*.1
    else:
      self.date = []
      self.temp = []
    
  def selectYear(self, year=2000):
    robj = meteo()
    _rtemp = [];
    for i, date in enumerate(self.date):
      if date.year == year:
	robj.date.append(date)
	_rtemp.append(self.temp[i])
    robj.temp = np.array(_rtemp)
    return robj
  
  def plotTemp(self, figure=None):
    if figure is None:
      fig = plt.figure()
      ax = fig.gca()
    else:
      fig = figure
      ax = fig.gca()

    ax.plot(self.date, self.temp, 'g')
    ax.grid(alpha=.6)

    ax.set_ylabel('Temperatur $^\circ$C')
    ax.set_ylim(-10, 30)
    
    fig.autofmt_xdate()

    ax.set_title('Temperaturaufzeichnung in Kiel-Holtenau')
    
    if figure is None:
      fig.show()

met = meteo('kl_10046_00_akt_txt.txt')

fig = plt.figure()
ax = fig.gca()
met.selectYear(2011).plotTemp(fig)

fig.set_size_inches(10,5)
fig.savefig('../fig/temperature-diagram_kiel.png', dpi=150)