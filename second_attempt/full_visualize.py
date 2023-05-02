import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# Reading the data from a CSV file using pandas
def np_piece_data_from_csv(num, piece, deriv=False):
    if deriv:
        filename = f'/Users/HAQbook/Desktop/graaaaphs/data/piano01_00{str(piece)}_p{str(num)}_d.csv' #performance number 1-6
    else:
        filename = f'/Users/HAQbook/Desktop/graaaaphs/data/piano01_00{str(piece)}_p{str(num)}.csv' #performance number 1-6
    repo = pd.read_csv(filename,header=0)
    columns=['Frame', 'Time (Seconds)']
    repo = repo.drop(columns, axis=1)

    cols_to_select = ~repo.columns.str.startswith("Unnamed")
    selected_cols = repo.loc[:, cols_to_select]
    # Create a new dataframe with the selected columns
    repo = pd.DataFrame(selected_cols)

    vals = repo.to_numpy(dtype=float)
    mask = np.isnan(vals)
    vals[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), vals[~mask])

    return repo, vals

def plotFrames():
    print('HI')
    '''plots all points in every frame in sequence'''
    plt.ion()    
    repo,vals = np_piece_data_from_csv(1,1)
    for i in range(1): #range(0, 10000, 200)
        xs = vals[i,0::3]
        ys = vals[i,1::3]
        zs = vals[i,2::3]
        LABELS = list(repo.columns[2::3])

        #pointLabels = repo.columns[0::3] 
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter(xs,ys,zs, c=zs, cmap='viridis', linewidth=0.5);

        for i, txt in enumerate(LABELS):
            ax.annotate(txt, (xs[i], ys[i]))

        plt.show()
        plt.pause(60.1)
        if 'ax' in globals(): ax.remove()
    plt.ioff()
    
#plotFrames()

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

from pylab import figure

 
repo,vals = np_piece_data_from_csv(1,1)
for j in range(1): #range(0, 10000, 200)
    xs = vals[j,0::3]
    ys = vals[j,1::3]
    zs = vals[j,2::3]
    LABELS = list(repo.columns[2::3])

    #pointLabels = repo.columns[0::3] 
    fig = figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(len(xs)): #plot each point + it's index as text above
        ax.scatter(xs[i],ys[i],zs[i],color='b') 
        ax.text(xs[i],ys[i],zs[i],  '%s' % (LABELS[i]), size=6, zorder=1, color='k') 


    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    pyplot.show()
