from matplotlib import pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import pandas as pd
from sklearn.preprocessing import normalize


def getDegrees2D(repo, vals, POINTSx):
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

def plot_degVStime2Ds(repo, vals, lisPOINTSx, ln):
    '''SINGLE DATASOURCE!! For each triplet ps=[p1,p2,p3] in list, plots angle between three points ps_n over all frames.'''
    X = np.linspace(0, ln//240, ln) # x-axis for graph: frame # -> seconds 
    for count,POINTSx in enumerate(lisPOINTSx):
        ang = getDegrees2D(repo, vals, POINTSx)
        plt.plot(X,ang,alpha=0.5, label=count) # generate plot
    plt.ylabel("Degrees")
    plt.xlabel("Time (sec)")
    plt.legend()
    plt.show()

def plot_degVStime2D(lisANGLES, lisLABELS, title=''):
    '''MULTI DATASOURCE!! For each array in lisANGLES, 
    plot them over length of the longest array over time.
    Label each line by the corresponding label from lisLABELS.'''
    plt.figure(figsize=(18, 5))
    for count,ang in enumerate(lisANGLES):
        ln = np.size(lisANGLES[count],0)
        X = np.linspace(0, ln//240, ln) # x-axis for graph: frame # -> seconds 
        plt.plot(X,ang,color=((6-count)/6,0.4,(count+1)/6,0.8), label=lisLABELS[count]) # generate plot
    plt.ylabel("Degrees")
    plt.xlabel("Time (sec)")
    plt.title(title)
    plt.legend()
    #plt.show()

def plot_degVSdeg2D(xPOINTSx,lisPOINTSx):
    '''For each triplet ps=[p1,p2,p3] in list, plots angle between three points ps_n over all frames.'''
    X = getDegrees2D(xPOINTSx) # x-axis for graph
    for count,POINTSx in enumerate(lisPOINTSx):
        ang = getDegrees2D(POINTSx)
        plt.plot(X,ang,alpha=0.5, label=count) # generate plot
    plt.ylabel("Degrees")
    plt.xlabel("Time (sec)")
    plt.legend()
    plt.show()

def plot3D(coordsX, coordsY, coordsZ, coarseness, ln):
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

def plotLimb3D(vals, limb, coarseness, ln):
    '''Plots a limb point over time in 3D'''
    x,y,z = np.array(vals[:,limb]),np.array(vals[:,limb+1]),np.array(vals[:,limb+2])
    plot3D(x,y,z, coarseness, ln)




'''

Column names of limbs that we care about atm:
- STRN
- LASI
- LSHO 
- LELB 
- LFIN
- LWRA
- LWRB

Reasonable triples for angles:
["LASI","LSHO","LELB"]
["LSHO","LELB","LWRA"]
["LELB","LWRA","LFIN"]


-------------CHOICES--------------
coarseness = 20 #min: 5 
len = np.size(vals,0) #max: np.size(vals,0)
limb = "LSHO"

a1 = p.getDegrees2D(repo, vals, ["LASI","LSHO","LELB"])
a2 = p.getDegrees2D(repo, vals, ["LSHO","LELB","LWRA"])
a3 = p.getDegrees2D(repo, vals, ["LELB","LWRA","LFIN"])

angleBetweens = [["LASI","LSHO","LELB"],["LSHO","LELB","LWRA"],["LELB","LWRA","LFIN"]]

-----------FUNC CALLS--------------
#p.plotLimb3D(vals, repo.columns.get_loc("piano_pilot_01:"+limb+"x"), coarseness, len)
#p.plot_degVStime2D(angleBetweens,len)
#p.plot3D(a1, a2, a3, coarseness, len)
#p.plot_degVSdeg2D(["LSHO","LELB","LWRA"],angleBetweens)

-------------------------


'''