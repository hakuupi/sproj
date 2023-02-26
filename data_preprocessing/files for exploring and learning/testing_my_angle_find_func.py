import numpy as np    
import pandas as pd
import matplotlib.pyplot as plt


data = [[0,0], [0,2], [2,2],[4,2],[2,4],[4,4]]
test_df = pd.DataFrame(data, columns=['x_dist', 'y_dist'])

def angle_find(row):
    if row.name < 2:
        return 0
    p1x,p1y,p2x,p2y,p3x,p3y = test_df.loc[row.name-2, 'x_dist'], test_df.loc[row.name-2, 'y_dist'], test_df.loc[row.name-1, 'x_dist'], test_df.loc[row.name-1, 'y_dist'], row['x_dist'], row['y_dist']
    
    vec1 = np.array([p2x-p1x, p2y-p1y])
    vec2 = np.array([p3x-p2x, p3y-p2y])
    ang = np.mod(np.arctan2(np.sum([[1,-1]]*vec1*vec2[::-1]), np.sum(vec1*vec2)),2*np.pi) * 180/np.pi
    ang = (ang + 180) % 360
    return ang

test_df['trajectories'] = test_df.apply (lambda row: angle_find(row), axis=1)

print("Results of my angles function on the toy example position data: ")
print(test_df['trajectories'])

