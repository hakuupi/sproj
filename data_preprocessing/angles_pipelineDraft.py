''' Uses data with n rows (frames), and 3*number of body points columns
Each frame is a row, and the columns are: 
bp1 x-coord, bp1 y-cord, and bp1 likelihood of those coordinates, 
then the same for bp2 etc...

Code:
Extract three columns and see the angle between these columns 
From matrix, extract x,y-coordinates for all three points for each frame, 
extract the angle between these points,
and plot a graph over time/frameID, and y-axis is angle.

Some helpful code to understand the data we're working with:
#print(list(dgroup.keys())) #['_i_table', 'table']
#print(dset.shape) #(3058,)
#print(dset.dtype) #[('index', '<i8'), ('values_block_0', '<f8', (90,))]
'''  
import numpy as np    
import matplotlib.pyplot as plt
from read_h5_data import read_h5_data
from write_degrees_from_raw_h5 import getDegrees
from savitzkyGolayFilter import filt

myDataset = '/Users/HAQbook/Documents/GitHub/sproj/data_files/example_antmovie_raw_data.h5'
# file is copy of: '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/antmovie220302180238DLC_resnet101_BU_trailApr4shuffle1_700000.h5'
vals, dTable, n = read_h5_data(myDataset)


def plotPoint(p):
    '''plots x,y,likelihood of a point p over all frames'''
    point_1 = p
    plt.plot(vals[:,point_1*3], label = "X position")
    plt.plot(vals[:,point_1*3+1], label = "Y position")
    plt.plot(vals[:,point_1*3+2], label = "Likelihood")
    plt.title(f"x,y,likelihood of point {point_1} over all frames")

def plotDegrees(ps, lbl=" "):
    '''plots the angle between three points ps=[p1,p2,p3] over all frames'''
    point_1 = int(ps[0])
    point_2 = int(ps[1])
    point_3 = int(ps[2])
    vec1 = vals[:,point_1*3:point_1*3+2] - vals[:,point_2*3:point_2*3+2]
    vec2 = vals[:,point_3*3:point_3*3+2] - vals[:,point_2*3:point_2*3+2]
    ang180 = np.arccos(np.sum(vec1*vec2,axis=1) / (np.linalg.norm(vec1,axis=1) * np.linalg.norm(vec2,axis=1))) * 180/np.pi #arccos approach to find angle,; gives angle between 0-180
    ang = np.mod(np.arctan2(np.sum([[1,-1]]*vec1*vec2[:,::-1],axis=1),
    np.sum(vec1*vec2,axis=1)),2*np.pi) * 180/np.pi #arctan approach to find angle; angle = arctan2(determinant ,dot product)

    plt.plot(ang,label=f"Angle between points {point_1}, {point_2}, and {point_3}. {lbl}",alpha=0.5)
    plt.ylabel("Degrees")

def plotFrames():
    '''plots all points in every frame in sequence'''
    for i in range(dTable.shape[0]):
        row = vals[i]
        xs = vals[i,0::3]
        ys = vals[i,1::3]

        pointLabels = [n for n in range(len(xs))]
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.scatter(xs,ys)    
        for i, txt in enumerate(pointLabels):
            ax.annotate(txt, (xs[i], ys[i]))   
        plt.plot(xs,y)



def pearsonCorrelationDegrees(psA,psB, lbl=" ", timeDelay=0):
    '''give pearson correlation coefficient between two angles over all frames'''
    p1,p2,p3,p4,p5,p6 = int(psA[0]), int(psA[1]), int(psA[2]), int(psB[0]), int(psB[1]), int(psB[2])
    td = int(timeDelay)
    vec1A = vals[td:,p1*3:p1*3+2] - vals[td:,p2*3:p2*3+2]
    vec2A = vals[td:,p3*3:p3*3+2] - vals[td:,p2*3:p2*3+2]
    vec1B = vals[:(n-td),p4*3:p4*3+2] - vals[:(n-td),p5*3:p5*3+2]
    vec2B = vals[:(n-td),p6*3:p6*3+2] - vals[:(n-td),p5*3:p5*3+2]
    angA = np.mod(np.arctan2(np.sum([[1,-1]]*vec1A*vec2A[:,::-1],axis=1),
    np.sum(vec1A*vec2A,axis=1)),2*np.pi) * 180/np.pi #arctan approach to find angle; angle = arctan2(determinant ,dot product)
    angB = np.mod(np.arctan2(np.sum([[1,-1]]*vec1B*vec2B[:,::-1],axis=1),
    np.sum(vec1B*vec2B,axis=1)),2*np.pi) * 180/np.pi
    corr = np.corrcoef(angA,angB)
    return(corr[0][1])

def plotCorrelation(dict,psA,psB, lbl=" "):
    '''plots two angles over all frames on x and y axis to each other per frame'''
    p1,p2,p3,p4,p5,p6 = int(dict[psA][0]), int(dict[psA][1]), int(dict[psA][2]), int(dict[psB][0]), int(dict[psB][1]), int(dict[psB][2])
    vec1A = vals[:,p1*3:p1*3+2] - vals[:,p2*3:p2*3+2]
    vec2A = vals[:,p3*3:p3*3+2] - vals[:,p2*3:p2*3+2]
    vec1B = vals[:,p4*3:p4*3+2] - vals[:,p5*3:p5*3+2]
    vec2B = vals[:,p6*3:p6*3+2] - vals[:,p5*3:p5*3+2]
    angA = np.mod(np.arctan2(np.sum([[1,-1]]*vec1A*vec2A[:,::-1],axis=1),
    np.sum(vec1A*vec2A,axis=1)),2*np.pi) * 180/np.pi #arctan approach to find angle; angle = arctan2(determinant ,dot product)
    angB = np.mod(np.arctan2(np.sum([[1,-1]]*vec1B*vec2B[:,::-1],axis=1),
    np.sum(vec1B*vec2B,axis=1)),2*np.pi) * 180/np.pi
    plt.scatter(angA,angB,label=f"{psA} and {psB}. {lbl}", alpha=0.5, marker='o')
    plt.title("Correlation dots: plots two angles over all frames on x and y axis to each other per frame")

def minSubPairDifference(a1, a2, a1index, r):
    "returns the index of the closest value of another list in a certain frame range"
    min_so_far = np.abs(a1[a1index]-a2[a1index])
    min_ending_here = 1000000
    min_index = a1index
       
    for i in range(r[1]):
        min_ending_here =  np.abs(a1[a1index]-a2[a1index+i])
        if (min_so_far > min_ending_here):
            min_so_far = min_ending_here
            min_index = a1index+i
    return min_index
def fancyPlotCorrelation(dict,psA,psB, lbl=" ", timeDelayRange=[0,0]):
    '''plots two angles over all frames on x and y axis to each other per frame, finding maximum correlation in range of frames'''
    p1,p2,p3,p4,p5,p6 = int(dict[psA][0]), int(dict[psA][1]), int(dict[psA][2]), int(dict[psB][0]), int(dict[psB][1]), int(dict[psB][2])
    vec1A = vals[:,p1*3:p1*3+2] - vals[:,p2*3:p2*3+2]
    vec2A = vals[:,p3*3:p3*3+2] - vals[:,p2*3:p2*3+2]
    vec1B = vals[:,p4*3:p4*3+2] - vals[:,p5*3:p5*3+2]
    vec2B = vals[:,p6*3:p6*3+2] - vals[:,p5*3:p5*3+2]
    angA = np.mod(np.arctan2(np.sum([[1,-1]]*vec1A*vec2A[:,::-1],axis=1),
    np.sum(vec1A*vec2A,axis=1)),2*np.pi) * 180/np.pi #arctan approach to find angle; angle = arctan2(determinant ,dot product)
    angB = np.mod(np.arctan2(np.sum([[1,-1]]*vec1B*vec2B[:,::-1],axis=1),
    np.sum(vec1B*vec2B,axis=1)),2*np.pi) * 180/np.pi
    plt.scatter(angA,angB,label=f"{psA} and {psB}. {lbl}", alpha=0.5, marker='o')
    plt.title("Plots two angles over all frames on x and y axis to each other per frame")



#----------------------------------------------------------------
limbs = {"antennaL0": [1,0,18], "antennaL1": [1,0,19], "antennaL2": [1,0,20],
"backLegL0": [3,2,29], "backLegL1": [3,2,28], "backLegL2": [3,2,27],
"frontLegL": [21,22,23], "midLegL": [24,25,26]}
# 20, 29 are not moving a lot
# 3,2,28 and 3,2,.27 should be correlated
# 3,2,29 should stay constant

#---uncleaned data stuff 
#plotDegrees(limbs["backLegL0"], "Stable [3,2,29] Back leg")
#plotDegrees(limbs["backLegL1"], "[3,2,28] Back leg")
#plotDegrees(limbs["backLegL2"], "[3,2,27] Back leg")

#plotDegrees(limbs["antennaL0"], "[1,0,18] Antenna L0")
#plotDegrees(limbs["antennaL1"], "[1,0,19] Antenna L1")
#plotDegrees(limbs["antennaL2"], "[1,0,20] Antenna L2")
#plotFrames()

#plotCorrelation(limbs,"antennaL0","antennaL1")
#plotCorrelation(limbs,"antennaL0","frontLegL")
#plotCorrelation(limbs,"antennaL0","midLegL")
#plotCorrelation(limbs,"antennaL0","backLegL0")

#---savgol stuff 
blL0 = getDegrees(limbs,"backLegL0",)
aL0 = getDegrees(limbs,"antennaL0",)
t,blL0_smoothed, lbl1 = filt(blL0, "backLegL0_smoothed_degrees", forder=9, wlen=21)
t,aL0_smoothed, lbl2 = filt(aL0, "antennaL0_smoothed_degrees", forder=9, wlen=21)

#plt.plot(t,blL0_smoothed, label=lbl1)
#plt.plot(t,aL0_smoothed, label=lbl2)
plt.scatter(blL0,aL0,label="Correlation blL0, aL0", alpha=0.5, marker='o')
plt.title("Correlation dots: plots two angles over all frames on x and y axis to each other per frame")


#---
plt.legend()
plt.show()






'''
for key,value in limbs.items():
    for antenna in ["antennaL1","antennaL2","antennaL3"]:
        for d in range(100):
            corr = pearsonCorrelationDegrees(limbs[antenna],value, timeDelay=d)
            if np.abs(corr) > 0.2:
                print('%-12s%-12s%-12s' % (f"{key} ({value}) and {antenna} ({limbs[antenna]}) correlation: ", corr, f", delay: {d} frames"))
            corr = pearsonCorrelationDegrees(value, limbs[antenna], timeDelay=d)
            if np.abs(corr) > 0.2:
                print('%-12s%-12s%-12s' % (f"{key} ({value}) and {antenna} ({limbs[antenna]}) correlation: ", corr, f", delay: -{d} frames"))

        print("")
'''

from sklearn.linear_model import LinearRegression
model = LinearRegression()
#model.fit(x, y)
