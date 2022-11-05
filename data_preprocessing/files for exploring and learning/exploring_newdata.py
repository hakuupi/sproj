import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

'''Plot, with a slider that varies the column choice, 
that visualises the data in newdata.csv. 
Run on the first n-rows of the data file.'''
n_rows=200
df = pd.read_csv('/Users/haqbook/Documents/GitHub/sproj/data_files/newData.csv', nrows=n_rows)
#df1 = df.head()
data = np.transpose(df.to_numpy())
labels = df.columns.values
t = data[1] #frames

print(len(data[3]))
print(labels)




y = data[3]

fig = plt.figure()
ax = fig.subplots()
p, = ax.plot(t,y, 'r')
ax.set_ylim([-50, 600])

ax_slide = plt.axes([0.25,0.1,0.65,0.03])
col_choice = Slider(ax_slide, 'column of newdata being plotted', valmin=0, valmax=256, valinit=2, valstep=1)

def update(val):
    current_v = int(col_choice.val)
    new_y = data[current_v]
    p.set_ydata(new_y)
    ax.set_ylim(np.min(new_y), np.max(new_y))
    plt.title(labels[current_v])
    fig.canvas.draw()
col_choice.on_changed(update)

'''
initial_text = "2"
def submit(text):
    xdata = int(eval(text))
    l.set_xdata(xdata)
    ax.set_xlim(np.min(xdata), np.max(xdata))
    fig.canvas.draw()
axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'Evaluate', initial=initial_text)
text_box.on_submit(submit)
'''

plt.show()