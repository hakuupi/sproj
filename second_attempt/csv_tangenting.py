import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

def removeOutliers(y):
    # Calculate the IQR fences
    #print(f'{np.min(y)=} and {np.max(y)=}')
    x = np.linspace(np.min(y), np.max(y), num=len(y)) #set of x values that cover the range of the data and are sufficiently dense to capture any rapid changes in the y values. 
    Q1 = np.percentile(y, 25)
    Q3 = np.percentile(y, 75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR

    # Smooth the outliers with linear interpolation
    outliers = (y < lower_fence) | (y > upper_fence) #boolean algebra
    x_outliers = x[outliers]
    f = interp1d(x[~outliers], y[~outliers], kind='linear', bounds_error=False, fill_value='extrapolate')
    y_smoothed = f(x_outliers)

    # Replace the outliers with the smoothed values
    y[outliers] = y_smoothed
    return(y)

def writeDeriv():
    '''Get first derivative of each segmented csv datafile, and export.'''
    path = '/Users/HAQbook/Documents/GitHub/sproj/second_attempt/data/'
    for piece in range(1,7):
        filename = 'piano01_00'+str(piece)+'_p'
        for performance in range(1,7):
            repo = pd.read_csv(path+filename+str(performance)+'.csv',sep=',',header=0)
            df = repo.diff()
            df.to_csv(path+filename+str(performance)+'_d'+'.csv')

def callDeriv(arrayLST, smoothed=False):
    '''Output list of first derivative arrays of inputted list of arrays'''
    output = []
    for a in arrayLST:
        if smoothed: # optional smoothing by numpy rolling average
            kernel_size = 80
            kernel = np.ones(kernel_size) / kernel_size
            a = np.convolve(a, kernel, mode='same') 
        grad = np.gradient(a) # could've used np.diff(a)
        grad_cleaner = removeOutliers(grad)
        output.append(grad_cleaner) 
    return(output)

