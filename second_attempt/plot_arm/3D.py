from matplotlib import pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import pandas as pd

# Data loading
def np_piece_data_from_csv(num, piece, deriv=False):
    if deriv:
        filename = f'/Users/HAQbook/Desktop/graaaaphs/data/piano01_00{str(piece)}_p{str(num)}_d.csv' 
    else:
        filename = f'/Users/HAQbook/Desktop/graaaaphs/data/piano01_00{str(piece)}_p{str(num)}.csv' 
    repo = pd.read_csv(filename,header=0)
    columns=['Frame', 'Time (Seconds)']
    repo = repo.drop(columns, axis=1)
    vals = repo.to_numpy(dtype=float)
    mask = np.isnan(vals)
    vals[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), vals[~mask])
    return repo, vals


# Actual stuff
def plot3D(coordsX, coordsY, coordsZ, coarseness, ln, TITLE : str = ''):
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

    N = ln//coarseness
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
    plt.title(TITLE)
    plt.show()

def plotLimb3D(repo, vals, limb, coarseness, ln, TITLE:str=''):
    '''Plots a limb point over time in 3D. 
    Note: Coarseness=n plots every nt frame'''
    lind = repo.columns.get_loc("piano_pilot_01:"+limb+"x")
    x,y,z = np.array(vals[:,lind]),np.array(vals[:,lind+1]),np.array(vals[:,lind+2])
    plot3D(x,y,z, coarseness, ln, TITLE)


# Main
def main():
    perf = 4
    piece = 5
    limb = "LSHO"
    repo,vals = np_piece_data_from_csv(perf, piece, deriv=False)
    print(len(vals))
    plotLimb3D(repo, vals, limb, 10, len(vals), TITLE=f"Position of {limb} on performance {perf} of piece {piece}")
if __name__ == '__main__':
    main()