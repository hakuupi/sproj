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

print(gdf.shape) # (2384, 5)
print(lvals.shape) # (2384, 90)

'''
I received the global data for the free foraging ants. 
The file contains: ['x_dist', 'y_dist', 'displacement', 'walked_dist', 'dist_food']
The format was not the same so I was a bit worried I couldn't match
the global datafiles with their local equivalents, but I checked a pair
of global/local files with the same dates and they were the same 
length! So I think I can safely associate angles gathered from 
each frame of the global data with the local data file. 
'''


'''
Next, I graphed x vs y dist to see what data I am working with. 

plt.plot(gdf['x_dist'],gdf['y_dist'])
plt.title("x vs y dist of a global data file")
plt.show()

It looks like a very reasonable trajectory, so x-dist and y-dist are
x and y coordinates of the ant in the arena for each frame.
'''

'''
Next, I get the trajectory of the ant at each time point, as the angle of the ant
over three consecutive time frames (insert rigorous definition of walks/paths 
used in graph theory?). # see diagram below (make diagram)
'''
def angle_find(row):
    if row.name < 3:
        return 0
    p1x,p1y,p2x,p2y,p3x,p3y = gdf.loc[row.name-2, 'x_dist'], gdf.loc[row.name-2, 'y_dist'], gdf.loc[row.name-1, 'x_dist'], gdf.loc[row.name-1, 'y_dist'], row['x_dist'], row['y_dist']
    
    vec1 = np.array([p2x-p1x, p2y-p1y])
    vec2 = np.array([p3x-p2x, p3y-p2y])
    ang = np.mod(np.arctan2(np.sum([[1,-1]]*vec1*vec2[::-1]), np.sum(vec1*vec2)),2*np.pi) * 180/np.pi
    ang = (ang + 180) % 360
    return ang

gdf['trajectories'] = gdf.apply (lambda row: angle_find(row), axis=1)


'''
To test if that worked as desired, let's graph the trajectory angles over time.

plt.plot(gdf['trajectories'])
plt.title("unedited trajectory angles over time")
plt.show()

We see that it looks very unstable, and it's still super messy...
Let's smooth it'''


gdf['smoothed_trajectories'] = savgolfilt(gdf['trajectories'],dorder = 0, forder = 5, wlen = 29)[1]

'''
plt.plot(gdf['smoothed_trajectories'])
plt.title("smoothed trajectory angles over time")
plt.show()


Now we can recognise where the angle lingers around 180 degrees
does match where the path trajectory is straight.
'''

gdf['extra_smoothed_trajectories'] = savgolfilt(gdf['trajectories'],dorder = 0, forder = 5, wlen = 15)[1]
plt.plot(gdf['extra_smoothed_trajectories'])
plt.title("smoothed trajectory angles over tim with window length 15")
plt.show()

'''
I wonder if I'm using the wrong smoothing filter for this purpose of finding intervals
of straight path. Maybe I should smooth the x,y coordinates and then get the angles instead.'''


def filter_indices(df):
    pass



# noise around ant might not be just as bad because it's local 
# here you're looking at the resolution around the path
# try: takng the path and do least squares
# try: make sure my angle fumction is correct by plotting the lines
# what are questions they would view as a result to be shared?