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

sampling_freq = 200  # in Hertz
chtypes = ['eeg', 'eeg', 'eeg', 'eeg', 'stim']
info = mne.create_info(chnames, sfreq=sampling_freq)



raw = mne.io.RawArray(data.T, info)
raw.plot(duration=1, highpass=0.01, lowpass=62.4)
raw.plot(n_channels=1, duration=1,show_scrollbars=False, show_scalebars=False)


stamps = pd.read_csv(data_stamp, skiprows=1)

start = stamps.loc[0][1]
onset = []
description=[]
duration=[]
#for all timestamps value, subtract start and add to onset
for x in range(len(stamps)):
  description.append(stamps.loc[x][0])
  ms = stamps.loc[x][1] - start
  onset.append(ms/1000) #why did i use math.floor??
  duration.append(0) 
print(onset)
print(description)

#
annotations = mne.Annotations(onset=onset, duration=duration, description=description)
raw.set_annotations(annotations)
# raw.plot(duration=onset[len(onset) -1], highpass=0.01, lowpass=30)
