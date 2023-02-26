import numpy as np    
import matplotlib.pyplot as plt
from read_h5_data import read_h5_data

myDataset = '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/free_DLC_data/05YYmajfd_antmovie200924211818DLC_resnet101_AntOct16shuffle1_3000000.h5'
# '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/antmovie220302180238DLC_resnet101_BU_trailApr4shuffle1_700000.h5'
vals, dTable, n = read_h5_data(myDataset)


'''point_1 = 1
plt.plot(vals[:,point_1*3], label = "X position")
plt.plot(vals[:,point_1*3+1], label = "Y position")
plt.plot(vals[:,point_1*3+2], label = "Likelihood")
plt.title(f"x,y,likelihood of point {point_1} over all frames")
'''

#vec1 = vals[:,point_1*3:point_1*3+2] - vals[:,point_2*3:point_2*3+2]



def plotFrames():
    '''plots all points in every frame in sequence'''
    plt.ion()    

    #for i in range(dTable.shape[0]):
    for i in range(0, 2000, 10):
        row = vals[i]
        xs = vals[i,0::3]
        ys = vals[i,1::3]

        pointLabels = [n for n in range(len(xs))]
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.scatter(xs,ys)    
        for i, txt in enumerate(pointLabels):
            ax.annotate(txt, (xs[i], ys[i]))   
        plt.plot(xs,ys)
        plt.pause(0.002)
        if 'ax' in globals(): ax.remove()

    plt.ioff()


plotFrames()
