## Python Script to deal with all preprocessing for .csv data obtained live from openbci
## We will be using MNE python for all of the preprocessing of data in this file, pandas to get it into the format that we need.

### Import statements
import mne
import pandas as pd
import numpy as np
import math
import random
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers.wrappers import TimeDistributed
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import AveragePooling2D
from keras.layers.recurrent import LSTM
from keras import regularizers
from keras.callbacks import ModelCheckpoint

### Data import statements
data_path = 'Testing Recordings\BrainFlow-RAW_2022-09-17_15-44-49_0.csv'
data_stamp = 'Testing Recordings\BrainFlow-RAW_2022-09-17_15-44-49_0.csv'


data = pd.read_csv(data_path, skiprows=1)
chnames = ['ch1', 'ch2', 'ch3', 'ch4', 'Timestamps']
