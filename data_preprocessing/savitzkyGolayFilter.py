from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

'''Notes:
-------Further to do this week:

- use 3D savgol on some random x,y columns vs frame #
- output to extra appended columns of datatable
- compare with their outputs

- figure out what columns they used in their code
- do that

- use savgol on ant data 
- do limb correlations after savgol on ant data
'''


def savgolfilt(data, newToVarList=[], varList=[], dorder=0, forder=3, wlen=15):
    '''Returns: (frame indices array, y_filtered array, labels).
    Inputs: data should be one column of a numpy array. (next step: accept one or more column!)
    varList the current labels of datatable in a list.
    newToVarList the titles of the new post filtering columns you want to add to the datatable.
    dorder is deriv, 
    forder is polyorder,
    and wlen is windowlength '''
    if type(newToVarList)!= list: newToVarList = [newToVarList]
    labels = varList + newToVarList

    t = np.indices(data.shape) #frames

    # applying the savitzky golay filter
    y = data
    y_filtered1 = savgol_filter(y, wlen, forder, deriv=dorder)
    return(t[0], y_filtered1, labels)

'''y = np.array([1,3,4,7,1,2,4,6,2,1,6,3,7,54,542,345,83,60,2,14,54,32,10])
b = ["a", "b"]
c = "test"
t,yNew, labels = filt(y,b,c)
print(t)
print(y)
print(yNew)
'''





def localsg( wlen, forder, dorder):
    '''Optimized Savitzky-Golay filter projection matrix computation'''
    pass
    #return(b)

def localsgfilt( x, b, wlen):
    '''Apply the Savitzky-Golay filter defined by the projection matrix b to
    data stored as columns of the matrix x. This implementation assumes that
    missing (NaN) values occur only at the beginning and end of timeseries'''
    pass
    #return(y)

def filt2(newData, varList, dorder, forder, wlen):
    '''SAVITZKYGOLAYFILTER: A function to smooth data and estimate derivatives
    using Savitzky-Golay filtering on a per-trajectory basis.'''
    # we input: savitzkyGolayFilter.filt(newData, pvl, 1, so, sl), where so=3, sl=15
    pass
    ##      Form       the       filter
    dt = 1 # note: dt is assumed to be unity

    #  Compute  the  projection  matrix
    b = localsg(wlen, forder, dorder) #in our case these are: wlen=15, forder=3, dorder=1

    # Scale  the  filter  appropriately
    if dorder > 0:
        b = b/(-dt)^dorder    #### do I have to turn this into numpy operations?

    ##  Apply  filter  to   the   data
    '''
    #Extract numerical data from table
    data = newData{:, varList};   

    #Find the groups corresponding to individual trajectories
    [G, ~] = findgroups(newData.uniqueFlyTrajID);

    # Estimate the derivatives for the timeseries of each trajectory
    [ dX ]= splitapply(@(x){localsgfilt( x, b, wlen )}, data, G);

    # Combine data for output
    dX = cat(1, dX{:});
    '''

    #return(dX)


'''
function [ b ] = localsg( wlen, forder, dorder )
% Optimized Savitzky-Golay filter projection matrix computation

% Validate inputs
if (round(wlen)~=wlen) || ~mod(wlen,2)
    error('Window length must be an odd integer.');
end
if forder > wlen - 1
    error('Filter order must be less than the window length minus one.');
end
if dorder > forder
    error('Derivative order must be less than or equal to the filter order.');
end

% Compute the half-window
halfwin = fix((wlen-1)/2);
x = (-halfwin:halfwin)';

% Form the Vandermonde matrix
v = x .^ (0:forder);

% Optimize for dorder = 0
if dorder == 0
    b = (v * (v \ eye(wlen)))';
else
    k = (1:(forder-dorder));
    hx = [(zeros(wlen,dorder)), ones(wlen,1)*prod(1:dorder), x.^k .* (k+1)];
    b = (hx * (v \ eye(wlen)))';
end
end

function [ y ] = localsgfilt( x, b, wlen )
% Apply the Savitzky-Golay filter defined by the projection matrix b to
% data stored as columns of the matrix x. This implementation assumes that
% missing (NaN) values occur only at the beginning and end of timeseries

% Allocate output
y = nan(size(x));
if size(x,1) > wlen
    % Find NaN rows
    xnotnan = ~any(isnan(x),2);
    if nnz(xnotnan) > wlen
        % Remove NaN rows
        x = x(xnotnan,:);
        
        % Compute the transient on
        ybegin = fliplr(b(:,(wlen-1)/2+2:end))' * flipud(x(1:wlen,:));
        
        % Compute the steady state output
        ycenter = filter(b(:,(wlen-1)./2+1), 1, x);
        
        % Compute the transient off
        yend = fliplr(b(:,1:(wlen-1)/2))' * flipud(x(end-(wlen-1):end,:));
        
        % Store output
        y(xnotnan,:) = [ybegin; ycenter(wlen:end,:); yend];
    end
end
end'''