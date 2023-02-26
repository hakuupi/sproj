import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt
from read_h5_data import read_h5_data
import csv
from savitzkyGolayFilter import savgolfilt

localData = '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/free_DLC_data/05YYmajfd_antmovie200924211818DLC_resnet101_AntOct16shuffle1_3000000.h5'
globalData = '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/filtered/successful_maj/antmovie200924211818_05YYmajfd_ys_038_foodloc_x2705_y1305_filtered.csv'

gdf = pd.read_csv (globalData)
lvals, ldTable, ln = read_h5_data(localData)
print(list(gdf.columns)) #['x_dist', 'y_dist', 'displacement', 'walked_dist', 'dist_food']


'''
I smooth x vs y dist to apply the angle finding on more reliable data.
I use a kernel moving average. 
'''

gdf['sX'] = gdf['x_dist'].rolling(20).mean()
gdf['sY'] = gdf['y_dist'].rolling(20).mean()

plt.plot(gdf['sX'],gdf['sY'])
plt.title("x vs y smoothed dists of a global data file")
plt.show()

'''
Next, I get the trajectory of the ant at each time point, as the angle of the ant
over three consecutive time frames (insert rigorous definition of walks/paths 
used in graph theory?). # see diagram below (make diagram)
'''
def angle_find(row):
    if row.name < 3:
        return 0
    p1x,p1y,p2x,p2y,p3x,p3y = gdf.loc[row.name-2, 'sX'], gdf.loc[row.name-2, 'sY'], gdf.loc[row.name-1, 'sX'], gdf.loc[row.name-1, 'sY'], row['sX'], row['sY']
    
    vec1 = np.array([p2x-p1x, p2y-p1y])
    vec2 = np.array([p3x-p2x, p3y-p2y])
    ang = np.mod(np.arctan2(np.sum([[1,-1]]*vec1*vec2),
    np.sum(vec1*vec2)),2*np.pi) * 180/np.pi
    return ang

gdf['trajectories'] = gdf.apply (lambda row: angle_find(row), axis=1)


'''
To test if that worked as desired, let's graph the trajectory angles over time.
'''


plt.plot(gdf['trajectories'])
plt.title("unedited trajectory angles over time, based on smoothed x,y dists")
plt.show()

'''
WTF!! It looks so different, I don't understand!
Welp, let's run with it.
'''



def filter_indices(df):
    pass
