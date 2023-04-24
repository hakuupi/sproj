import matplotlib.pyplot as plt

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

for i in range(5):

    ax1.plot(xs_a[i], ys_a[i], label='line' + str(i))
    ax2.plot(xs_b[i], ys_b[i], label='line' + str(i))

plt.setp( ax1.xaxis.get_majorticklabels(), rotation=90)
plt.setp( ax2.xaxis.get_majorticklabels(), rotation=90)

fig1.show()
fig2.show()