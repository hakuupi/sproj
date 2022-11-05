'''Preprocessing the dataset:
- Calculate smoothed versions of the phase and frequency variables and the centroid velocity components
- Remove frames in which the fly stops
Original matlab code is in 'GaitPaperFiguresScript.mlx' and fails to run.
'''
from read_data import *
from filterData import *
import numpy as np

data = read_data('/Users/haqbook/Documents/GitHub/sproj/data_files/newData.csv')
print(data[3])
cleanData = filterData(data)

# export data in .mat format, so that I can then try to run the figure plots in matlab with their code.


'''Notes:
- 
'''












