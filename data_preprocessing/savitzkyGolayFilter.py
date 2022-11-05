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







def filt(newData, varList, dorder, forder, wlen):
    # get noisy signal
    pass
'''
# applying the savitzky golay filter
y_filtered1 = savgol_filter(y, 99, 3)

# plot noisy and cleaned of various window lengths
fig = plt.figure()
ax = fig.subplots()
p0 = ax.plot(x,y, '-*')
p, = ax.plot(x,y_filtered1, 'g')

ax_slide = plt.axes([0.25,0.1,0.65,0.03])
win_len = Slider(ax_slide, 'Window length', valmin=5, valmax=99, valinit=99, valstep=2)

def update(val):
    current_v = int(win_len.val)
    new_y = savgol_filter(y, current_v, 3)
    p.set_ydata(new_y)
    fig.canvas.draw()
win_len.on_changed(update)
plt.show()
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