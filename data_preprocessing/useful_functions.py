import pandas as pd

'''THIS FUNCTION HAS PROBLEMS!!!!! DO NOT USE UNTIL YOU'VE FIXED IT!!!'''



def read_data(filename):
    df = pd.read_csv(filename, nrows=200)
    data = df.to_numpy()
    flyID = data[:,0]
    frame = data[:,1]
    features = data[:1:]
    return flyID, frame, features, df.columns.values



'''Documenting my work:
- Attempted to import file in python directly, 
but this hit upon a problem with the .mat file being too old 
('mat4py.loadmat.ParseError: Can only read from Matlab level 5 MAT-files'), 
and was also not very pretty. 

import h5py
import mat4py

f = mat4py.loadmat('/Users/haqbook/Desktop/papers_murthyLab/fliesData/20181025_20180530-20180614_IsoD1_Glass_MaskedModel_1000PCs_amplitude_phase_down_downcam_Steps(_down_cam).mat')
# mat4py.loadmat.ParseError: Can only read from Matlab level 5 MAT-files

#f = h5py.File('/Users/haqbook/Desktop/papers_murthyLab/fliesData/20181025_20180530-20180614_IsoD1_Glass_MaskedModel_1000PCs_amplitude_phase_down_downcam_Steps(_down_cam).mat','r')

newData = pd.DataFrame(f)
#newData = np.array(f) # For converting to a NumPy array
----------

- Solution: export data to csv in matlab (writetable(newData, 'newData.csv'), 
and read in a csv to my python script.

import pandas as pd
df = pd.read_csv('/Users/haqbook/Documents/GitHub/sproj/newData.csv')
newData = df.to_numpy()
----------

- csv turned out to triple the datafile size from 2.34 gb to over 6 gb. 
So I asked a friend to download the mat2np app on their not-locked matlab 
and thereby avoid the annoying step of huge-csv-loading. 
Unfortunately the table headings had to be lost, 
and it is still too large to be workable while I'm creating the environment. 

mat2np(newData, 'newData.pkl', float64)

import pickle
import numpy as np
print('code is running')

pickleFile = open('/Users/haqbook/Documents/GitHub/sproj/newData.pkl','rb')
newData = pickle.load(pickleFile)
----------

- Decided to just import the first 200 rows of the csv as a df for now.

'''