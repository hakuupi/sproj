import pandas as pd
import numpy as np

# Reading the data from CSV
repo = pd.read_csv('/Users/HAQbook/Documents/GitHub/sproj/second_attempt/data/piano01_003clean.csv',sep=',',header=0)
columns=['Frame', 'Time (Seconds)']
time = repo[columns]  
repo = repo.drop(columns, axis=1)
vals = repo.to_numpy(dtype=float)

# Fill in NaN's...
mask = np.isnan(vals)
vals[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), vals[~mask])
