import numpy as np    
from read_h5_data import *

myDataset = '/Users/HAQbook/Documents/GitHub/sproj/data_files/example_antmovie_raw_data.h5'
# file is copy of: '/Users/HAQbook/Desktop/depth_stuff/deeplabcut_stuff/antmovie220302180238DLC_resnet101_BU_trailApr4shuffle1_700000.h5'
vals, dTable, n = read_h5_data(myDataset)

def getDegrees(dict,ps):
    '''writes [m rows, 1 column] numpy array with the angle between three points ps=[p1,p2,p3] over all m frames'''
    point_1 = int(dict[ps][0])
    point_2 = int(dict[ps][1])
    point_3 = int(dict[ps][2])
    vec1 = vals[:,point_1*3:point_1*3+2] - vals[:,point_2*3:point_2*3+2]
    vec2 = vals[:,point_3*3:point_3*3+2] - vals[:,point_2*3:point_2*3+2]
    #ang180 = np.arccos(np.sum(vec1*vec2,axis=1) / (np.linalg.norm(vec1,axis=1) * np.linalg.norm(vec2,axis=1))) * 180/np.pi #arccos approach to find angle,; gives angle between 0-180
    ang = np.mod(np.arctan2(np.sum([[1,-1]]*vec1*vec2[:,::-1],axis=1),
    np.sum(vec1*vec2,axis=1)),2*np.pi) * 180/np.pi #arctan approach to find angle; angle = arctan2(determinant ,dot product)
    return(ang)