import matplotlib.pyplot as plt 
import pandas as pd

# Reading the data from a CSV file using pandas
repo = pd.read_csv('/Users/HAQbook/Documents/GitHub/sproj/second_attempt/piano01_003clean.csv',sep=',',header=0)
columns=['Frame', 'Time (Seconds)']
time = repo[columns]
repo = repo.drop(columns, axis=1)
vals = repo.to_numpy(dtype=float)

def plotFrames():
    print('HI')
    '''plots all points in every frame in sequence'''
    plt.ion()    
    for i in range(1): #range(0, 10000, 200)
        xs = vals[i,0::3]
        ys = vals[i,1::3]
        zs = vals[i,2::3]
        #pointLabels = repo.columns[0::3] 
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter(xs,ys,zs, c=zs, cmap='viridis', linewidth=0.5);
        plt.show()
        plt.pause(10.1)
        if 'ax' in globals(): ax.remove()
    plt.ioff()
    
plotFrames()
