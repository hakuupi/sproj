import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

'''
A: uses 2D savgol with slider for window length 
on a column of newdata vs frame and plots it.

B: uses 2D savgol with slider for choice of column of newdata 
on a column of newdata vs frame, using nominal window length=15 
and plots it.

Run at bottom.
'''

def A(n_rows,col_choice, degr):
    # load data
    df = pd.read_csv('/Users/haqbook/Documents/GitHub/sproj/data_files/newData.csv', nrows=n_rows)
    data = np.transpose(df.to_numpy())
    labels = df.columns.values
    t = data[1] #frames

    # applying the savitzky golay filter
    y = data[col_choice]
    y_filtered1 = savgol_filter(y, 15, degr, deriv=0)
    y_filtered2 = savgol_filter(y, 15, degr, deriv=1)

    # plot data of nth column with variable window length
    fig = plt.figure()
    ax = fig.subplots()
    p0 = ax.plot(t,y, '-*')
    p1 = ax.plot(t,y_filtered1, '-*')
    p, = ax.plot(t,y_filtered2, 'r')
    plt.title("Plot smoothed vs unsmoothed "+ labels[col_choice])

    ax_slide = plt.axes([0.25,0.1,0.65,0.03])
    win_len = Slider(ax_slide, 'Window length', valmin=5, valmax=n_rows-1, valinit=15, valstep=2)

    def update(val):
        current_v = int(win_len.val)
        new_y = savgol_filter(y, current_v, 3)
        p.set_ydata(new_y)
        fig.canvas.draw()
    win_len.on_changed(update)
    plt.show()


def B(n_rows, w_len, degr):
    # load data
    df = pd.read_csv('/Users/haqbook/Documents/GitHub/sproj/newData.csv', nrows=n_rows)
    data = np.transpose(df.to_numpy())
    labels = df.columns.values
    t = data[1] #frames

    # applying the savitzky golay filter
    y = data[2]
    y_filtered1 = savgol_filter(y, w_len, degr)

    # plot data of nth column with variable window length
    fig = plt.figure()
    ax = fig.subplots()
    p0, = ax.plot(t,y, '-*')
    p, = ax.plot(t,y_filtered1, 'r')
    plt.title("Plot smoothed vs unsmoothed "+ labels[2])

    ax_slide = plt.axes([0.25,0.1,0.65,0.03])
    col_choice = Slider(ax_slide, 'column of newdata being plotted', valmin=0, valmax=256, valinit=2, valstep=1)

    def update(val):
        current_v = int(col_choice.val)
        new_y = data[current_v]
        p0.set_ydata(new_y)
        new_y_filtered = savgol_filter(new_y, w_len, 3)
        p.set_ydata(new_y_filtered)

        ax.set_ylim(np.min(new_y), np.max(new_y))
        plt.title("Plot smoothed vs unsmoothed "+labels[current_v])
        fig.canvas.draw()
    col_choice.on_changed(update)
    plt.show()


#----------------------------
def main():
    #   setting   hyperparameters 
    nRows=25*2         # choose how many rows of newdata to load. Force choosing an even number for the window length.
    degree=3
    # for function A
    colChoice = 101     # choose which data column of newdata to plot
    # for function B
    wLen=5             # choose window length

    #      call        functions
    A(nRows,colChoice, degree)
    #B(nRows,wLen, degree)

if __name__ == "__main__":
    main()