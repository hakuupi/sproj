import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import StepPatch


A = [[0, 0, 0],
     [1, 2, 3],
     [2, 4, 6],
     [3, 6, 9]]

for i in range(len(A) - 1):
    plt.stairs(A[i+1], baseline=A[i], fill=True)

plt.show()