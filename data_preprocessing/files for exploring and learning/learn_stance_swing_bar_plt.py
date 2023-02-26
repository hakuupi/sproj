import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections
from read_h5_data import read_h5_data

myDataset = '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/free_DLC_data/05YYmajfd_antmovie200924211818DLC_resnet101_AntOct16shuffle1_3000000.h5'
# '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/antmovie220302180238DLC_resnet101_BU_trailApr4shuffle1_700000.h5'
vals, dTable, n = read_h5_data(myDataset)

l1,l2,l3,r1,r2,r3 = vals[:,21*3:24*3+2], vals[:,24*3:24*3+2], vals[:,27*3:27*3+2], vals[:,8*3:8*3+2], vals[:,11*3:11*3+2], vals[:,14*3:14*3+2]


'''when the angle: (limb, to body center, to point in front of ant body center) 
decreasing, mark as swing.
Else, mark as stance (??)
'''

# Horizontal bar plot with gaps
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 5), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (15, 5),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))


t = np.arange(0.0, 100, 0.01)
s1 = np.sin(2*np.pi*t)
collection = collections.BrokenBarHCollection.span_where(
    t, ymin=30, ymax=35, where=s1 > 0, facecolor='green') # , alpha=0.5
ax.add_collection(collection)


ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('time')
ax.set_yticks([10, 15, 20,25,30,35], labels=['','','','','',''])     
ax.set_yticks([7, 12, 17, 22, 27, 32], labels=['R3','R2','R1','L3','L2','L1'], minor=True)     # Modify y-axis tick labels
ax.grid(True)  # Make grid lines visible
plt.show()
