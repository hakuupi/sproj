import h5py    
import numpy as np    

def read_h5_data(myDataset):
    'Returns numpy array of values of the dataset'
    f = h5py.File(myDataset,'r+')    
    dGroup = f['df_with_missing']
    dTable = dGroup['table']
    indices = dTable.fields("index")
    values = dTable.fields("values_block_0")
    vals = np.stack(values) 
    n = vals.shape[0]
    return(vals,dTable,n)