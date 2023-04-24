import plot_arm as p
import pandas as pd
import csv_tangenting as t
from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq #outputs half

# Reading the data from CSV

#repo = pd.read_csv('/Users/HAQbook/Documents/GitHub/sproj/second_attempt/data/piano01_003interp.csv',sep=',',header=0)
def np_piece_data_from_csv(num, piece):
    path = '/Users/HAQbook/Documents/GitHub/sproj/second_attempt/data/'
    filename = 'piano01_00'+str(piece)+'_p'+str(num) #performance number 1-6
    repo = pd.read_csv(path+filename+'.csv',sep=',',header=0)
    columns=['Frame', 'Time (Seconds)']
    repo = repo.drop(columns, axis=1)
    #repo = repo.drop(index=[0,1])
    vals = repo.to_numpy(dtype=float)
    return(repo,vals)



'''Column names of limbs that we care about atm:
- STRN
- LASI
- LSHO 
- LELB 
- LFIN
- LWRA
- LWRB'''

'''Reasonable triples for angles:
["LASI","LSHO","LELB"]
["LSHO","LELB","LWRA"]
["LELB","LWRA","LFIN"]
'''

'''-------------CHOICES--------------'''
angLSHO = ["LASI","LSHO","LELB"]
angLELB = ["LSHO","LELB","LWRA"]
angLWRA = ["LELB","LWRA","LFIN"]
angRSHO = ["RASI","RSHO","RELB"]
angRELB = ["RSHO","RELB","RWRA"]
angRWRA = ["RELB","RWRA","RFIN"]

coarseness = 20 #min: 5 

'''-----------FUNC CALLS--------------'''
''' # Smoothed-derivative plotting things?
for piece in [1,2,3,5,6]:
    angLST = [angLSHO,angLELB,angLWRA,angRSHO,angRELB,angRWRA] # list of angles to loop through
    # the 6 performances of a piece; repo(df) and vals(np array)
    p1,p2,p3,p4,p5,p6 = np_piece_data_from_csv(1,piece),np_piece_data_from_csv(2,piece),np_piece_data_from_csv(3,piece),np_piece_data_from_csv(4,piece),np_piece_data_from_csv(5,piece),np_piece_data_from_csv(6,piece) # the 6 performances of a piece; repo(df) and vals(np array)

    for ang in angLST:
        angpick = ang
        limbName = angpick[1]
        a1,a2,a3,a4,a5,a6 = p.getDegrees2D(p1[0], p1[1], angpick),p.getDegrees2D(p2[0], p2[1], angpick),p.getDegrees2D(p3[0], p3[1], angpick),p.getDegrees2D(p4[0], p4[1], angpick),p.getDegrees2D(p5[0], p5[1], angpick),p.getDegrees2D(p6[0], p6[1], angpick)
        arrayLST = [a1,a2,a3,a4,a5,a6]
        [a1,a2,a3,a4,a5,a6] = t.callDeriv(arrayLST,smoothed=True)
        pl = p.plot_degVStime2D([a1,a2,a3,a4,a5,a6], ['p1','p2','p3','p4','p5','p6'], "Change in "+limbName+" angle over performances 1 through 6 of Piece #"+str(piece)+ "(Smoothed over 20 frame rolling average)")
        plt.savefig('/Users/HAQbook/Desktop/graaaaphs/d20_'+limbName+'ang_piece'+str(piece)+'_2D.png')
'''


#Frequency plotting things
angLST = [angLSHO,angLELB,angLWRA,angRSHO,angRELB,angRWRA] # list of angles to loop through
limbLST = ['LSHO','LELB','LWRA','RSHO','RELB','RWRA'] # list of angles to loop through


from sklearn.decomposition import PCA
def pca(X):
    # Flatten the 3D array to a 2D array
    X_flat = X.reshape(X.shape[0], -1)
    # Create a PCA object
    pca = PCA(n_components=1)
    # Fit the PCA object to the data and transform the data
    X_projected = pca.fit_transform(X_flat)
    # Return the projected data
    return X_projected.flatten()



# single frequency plot for fixed piece and performance
piece = 3
perf = 3
p1 = np_piece_data_from_csv(perf,piece)
p1a = p1[0]
plt.clf() 
print(p1[0].columns)

for j,limb in enumerate(limbLST):
    #a = p.getDegrees2D(p1[0], p1[1], limb)
    xInd = p1a.columns.get_loc("piano_pilot_01:"+limb+"x")
    y = np.array(p1[1][:,xInd:xInd+3])
    x = pca(y)
    sr = 240
    N = np.size(x) # number of samples
    yf = rfft(x)
    xf = rfftfreq(N, 1/sr)
    #plt.plot(xf, np.abs(yf),color=((6-j)/6,0.4,(j+1)/6,0.8), label=limb) # generate plot, abs because yfs are complex
    print(limb)
plt.legend()
plt.title(str(" performance " +str(perf) +" piece " +str(piece)))
plt.xlim(0.25,4)
plt.ylim(0,15040)
    #plt.savefig('/Users/HAQbook/Desktop/graaaaphs/frequencies_piece'+str(piece)+'.png')
plt.show()

#repo,vals = np_piece_data_from_csv(3, 5)
#limb = "LSHO"
#ln = 2400


#angleBetweens = [["LASI","LSHO","LELB"],["LSHO","LELB","LWRA"],["LELB","LWRA","LFIN"]]

#p.plotLimb3D(vals, repo.columns.get_loc("piano_pilot_01:"+limb+"x"), coarseness, ln)
#p.plot_degVStime2D(repo, vals, angleBetweens,len)
#p.plot3D(a1, a2, a3, coarseness, len)
#p.plot_degVSdeg2D(["LSHO","LELB","LWRA"],angleBetweens)

'''-------------------------'''