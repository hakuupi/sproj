import matplotlib.pyplot as plt

# Horizontal bar plot with gaps
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 5), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (15, 5),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))


ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('time')
ax.set_yticks([10, 15, 20,25,30,35], labels=['','','','','',''])     
ax.set_yticks([7, 12, 17, 22, 27, 32], labels=['R3','R2','R1','L3','L2','L1'], minor=True)     # Modify y-axis tick labels
ax.grid(True)  # Make grid lines visible
plt.show()

''' #Cool annotation stuff
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')
'''