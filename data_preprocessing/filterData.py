'''function [ newData ] = filterData( newData, so, sl, gl, gs, ms, use_moving_average )
FILTERDATA This function applies all needed smoothing and filtering to 
various variables in the data table and appends the results to the table.
'''
import savitzkyGolayFilter


def filterData(newData, so=3, sl=15, gl=15, gs=3, ms=5, use_moving_average=False):
    ##  Smooth  phases  and  approximate  frequencies

    limbList = ['L1','L2','L3','R1','R2','R3'] # columns 1 through 6
    limbList = [s + 'x' for s in limbList] + [s + 'y' for s in limbList] # columns 1 through 12

    pvl = ['InstantaneousPhase_' + s for s in limbList]
    fvl = ['InstantaneousFrequency_' + s for s in limbList]
    avl = ['InstantaneousAmplitude_' + s for s in limbList]

    spvl = ['smooth_' + s for s in pvl]
    sfvl = ['smooth_' + s for s in fvl]
    savl = ['smooth_' + s for s in avl]

    # Approximate   instantaneous   frequencies
    output = savitzkyGolayFilter.filt(newData, pvl, 1, so, sl)
    print('Approximated instantaneous frequencies')

    #     Smooth      instantaneous      phases

    #    Smooth     instantaneous    amplitudes


'''
% Approximate instantaneous frequencies

What does the notation, newData{:, sfvl}, mean?
What is the output?

size([ newData{:, sfvl} ] = 1767961    12
class([ newData{:, sfvl} ] = double

post savitzky:
Columns 1 through 3:
NaN      NaN      NaN    
NaN      NaN      NaN    
NaN      NaN      NaN  
0.0483   -0.2028  -0.0610
0.0369   -0.1347  0.0206
etc



% Smooth instantaneous phases
tic;
[ newData{:, spvl} ] = savitzkyGolayFilter( newData, pvl, 0, so, sl );
fprintf('Smoothed instantaneous phases in %f seconds.\n', toc);

% Smooth instantaneous amplitudes
tic;
[ newData{:, savl} ] = SmoothWithMovingAverageFilter(newData, avl, ms);
fprintf('Smoothed instantaneous amplitudes in %f seconds.\n', toc);

'''



    # #     Smooth       centroid       dynamics

    #      Smooth        centroid        traces

    







'''--Tuesday, 18 october--
I set the nominal values for the filterData function. 
Sketched out the parts of the filerData function.

'''

'''--Sunday, 23 october--
I am working on the 'smooth phases and approximate frequencies' part 
of the filterData function. 
I am learning matlab syntax along the way.
Apparently, their savitzkyGolayFilter is custom too, so I will 
have to look into that next, in order to do this filterData function.




'''

'''Matlab Syntax:
s = strcat(s1,...,sN); #%Concatenate strings horizontally

firstnames = {'Abraham'; 'George'};
lastnames = {'Lincoln'; 'Washington'};
commas = {', '};
names = strcat(lastnames, commas, firstnames)
--> names = 2x1 cell
    {'Lincoln, Abraham'  }
    {'Washington, George'}

x = [1 2 3]; #% matrix with values 1, 2, 3
y = {1, 'a', x}; #% cell array storing a number, a character, and 1x3 matrix

[y1,...,yN] = myfun(x1,...,xM) #% declares a function named myfun 
that accepts inputs x1,...,xM and returns outputs y1,...,yN.

'''
