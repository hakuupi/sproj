from matplotlib import pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import pandas as pd
from sklearn.preprocessing import normalize

def getDegrees2D(POINTSx):
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

def plot_degVStime2D(lisPOINTSx, len):
    '''For each triplet ps=[p1,p2,p3] in list, plots angle between three points ps_n over all frames.'''
    X = np.linspace(0, len//240, len) # x-axis for graph: frame # -> seconds 
    for count,POINTSx in enumerate(lisPOINTSx):
        ang = getDegrees2D(POINTSx)
        plt.plot(X,ang,alpha=0.5, label=count) # generate plot
    plt.ylabel("Degrees")
    plt.xlabel("Time (sec)")
    plt.legend()
    plt.show()

def plot_degVSdeg2D(xPOINTSx,lisPOINTSx):
    '''For each triplet ps=[p1,p2,p3] in list, plots angle between three points ps_n over all frames.'''
    X = getDegrees2D(xPOINTSx) # x-axis for graph: frame # -> seconds 
    for count,POINTSx in enumerate(lisPOINTSx):
        ang = getDegrees2D(POINTSx)
        plt.plot(X,ang,alpha=0.5, label=count) # generate plot
    plt.ylabel("Degrees")
    plt.xlabel("Time (sec)")
    plt.legend()
    plt.show()

def plot3D(coordsX, coordsY, coordsZ, coarseness, len):
    '''Plots a three 1D arrays as a point over time in 3D'''
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d') # 3D plotting things

    def gen(n, coarseness, xyz_data):
        i = 0
        while i < n:
            yield np.array(xyz_data[i*coarseness]) 
            i += 1

    def update(num, data, line): # More 3D plotting things
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = len//coarseness
    xyz_data = np.stack((coordsX, coordsY, coordsZ), axis=1)
    data = np.array(list(gen(N,coarseness,xyz_data))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

    # Setting the axes properties
    ax.set_xlim3d([np.min(xyz_data[:,0]), np.max(xyz_data[:,0])])
    ax.set_xlabel('X')

    ax.set_ylim3d([np.min(xyz_data[:,1]), np.max(xyz_data[:,1])])
    ax.set_ylabel('Y')

    ax.set_zlim3d([np.min(xyz_data[:,2]), np.max(xyz_data[:,2])])
    ax.set_zlabel('Z')

    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N, blit=False)
    #ani.save('matplot003.gif', writer='imagemagick')
    plt.show()

def plotLimb3D(vals, limb, coarseness, len):
    '''Plots a limb point over time in 3D'''
    x,y,z = np.array(vals[:,limb]),np.array(vals[:,limb+1]),np.array(vals[:,limb+2])
    plot3D(x,y,z, coarseness, len)

