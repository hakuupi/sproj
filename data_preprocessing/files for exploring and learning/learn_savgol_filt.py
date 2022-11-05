from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

'''Plot, with a slider that varies the window length, that shows
how savitzky golay filter (here forth abbreviated savgol) 
works on simple, 2D, self-generated noisy signal, 
seeing how the smoothing varied with the window length 
primarily, and the polynmial degree secondarily.'''

# generate noisy signal 
x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + np.cos(x) + np.random.random(100)

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

