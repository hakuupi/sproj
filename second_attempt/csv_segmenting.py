'''Segment the cleaned and interpolated csv datafiles by 
the timestamps of another timestamp csv file into the six pieces'''

import numpy as np
import pandas as pd

path = '/Users/HAQbook/Documents/GitHub/sproj/second_attempt/data/'
filename = 'piano01_002interp'
repo = pd.read_csv(path+filename+'.csv',sep=',',header=0)

timestamps = pd.read_csv('/Users/HAQbook/Documents/GitHub/sproj/second_attempt/performance_timestamps.csv',sep=',',header=0)
piece = 2

tcolumns = list(timestamps.columns)
performancesIndices = [2,4,8,10,12,14]

for i in range(6):
    start = timestamps.iloc[piece-1,performancesIndices[i]]
    stop = timestamps.iloc[piece-1,performancesIndices[i]+1]
    df = repo.iloc[start*240:stop*240,:]
    #print(str(i+1)+': '+ str(df.shape))
    df.to_csv(path+'piano01_002_p'+str(i+1)+'.csv')

# vals[:,limb+1]

