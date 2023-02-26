import plot_arm as p
import numpy as np
import pandas as pd


# Reading the data from CSV
repo = pd.read_csv('/Users/HAQbook/Documents/GitHub/sproj/second_attempt/piano01_003clean.csv',sep=',',header=0)
columns=['Frame', 'Time (Seconds)']
time = repo[columns]  
repo = repo.drop(columns, axis=1)
vals = repo.to_numpy(dtype=float)

# Fill in NaN's...
mask = np.isnan(vals)
vals[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), vals[~mask])


'''Column names of limbs that we care about atm:
- STRN
- LASI
- LSHO 
- LELB 
- LFIN
- LWRA
- LWRB'''

'''Reasonable triples for angles:
["LASI","LSHO","LELB"]
["LSHO","LELB","LWRA"]
["LELB","LWRA","LFIN"]
'''

'''-------------CHOICES--------------'''
coarseness = 20 #min: 5 
len = np.size(vals,0) #max: np.size(vals,0)
limb = "LSHO"

a1 = p.getDegrees2D(["LASI","LSHO","LELB"])
a2 = p.getDegrees2D(["LSHO","LELB","LWRA"])
a3 = p.getDegrees2D(["LELB","LWRA","LFIN"])

angleBetweens = [["LASI","LSHO","LELB"],["LSHO","LELB","LWRA"],["LELB","LWRA","LFIN"]]

'''-----------FUNC CALLS--------------'''
#p.plotLimb3D(vals, repo.columns.get_loc("piano_pilot_01:"+limb+"x"), coarseness, len)
#p.plot_degVStime2D(angleBetweens,len)
#p.plot3D(a1, a2, a3, coarseness, len)
p.plot_degVSdeg2D(["LSHO","LELB","LWRA"],angleBetweens)

'''-------------------------'''