import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import normalize


def np_piece_data_from_csv(num, piece, deriv=False):
    if deriv:
        filename = f'data/piano01_00{str(piece)}_p{str(num)}_d.csv' #performance number 1-6
    else:
        filename = f'data/piano01_00{str(piece)}_p{str(num)}.csv' #performance number 1-6
    repo = pd.read_csv(filename,header=0)
    columns=['Frame', 'Time (Seconds)']
    repo = repo.drop(columns, axis=1)
    vals = repo.to_numpy(dtype=float)
    mask = np.isnan(vals)
    vals[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), vals[~mask])
    return repo, vals

def getDegrees2D(repo, vals, POINTSx): # duplicate in 'degrees2D.ipynb'
    '''Gets angle between three points ps=[p1,p2,p3] over all frames'''
    p1x = repo.columns.get_loc("piano_pilot_01:"+POINTSx[0]+"x") # get the x,y,z data for each of the three points over all frames
    p2x = repo.columns.get_loc("piano_pilot_01:"+POINTSx[1]+"x")
    p3x = repo.columns.get_loc("piano_pilot_01:"+POINTSx[2]+"x")

    def unit_vector(vector):
        '''helper function to normalise vectors'''
        return normalize(vector, axis=1, norm='l2')

    v1 = vals[:,p1x:p1x+3] - vals[:,p2x:p2x+3] # 3 points -> 2 vectors
    v2 = vals[:,p3x:p3x+3] - vals[:,p2x:p2x+3]
    v1_u = unit_vector(v1) # vectors -> unit vectors
    v2_u = unit_vector(v2)
    ang = np.rad2deg(np.arccos(np.sum(v1_u*v2_u, axis=1))) # calculate angle between vectors
    return(ang) 

perf = 1
piece = 5
limb = ["LASI","LSHO","LELB"]
repo, vals = np_piece_data_from_csv(perf,piece)
signal = getDegrees2D(repo, vals, POINTSx = limb)

sample_rate = 240
max_time = signal.size/sample_rate

time_steps = np.linspace(0, max_time, signal.size)
plt.figure()
plt.plot(time_steps, signal)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

f = np.abs(np.fft.rfft(signal))
freq_steps = np.fft.rfftfreq(signal.size, d=1/sample_rate)
plt.figure()
plt.plot(freq_steps, f)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.xlim(0,4)
plt.show()