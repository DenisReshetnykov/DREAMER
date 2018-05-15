import numpy as np
import scipy.io as sio
import pandas as pd



def load_data(datafile):
    data = sio.loadmat(datafile)
    return data

print(load_data(DREAMER.mat))