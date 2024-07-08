import pandas as pd
import os
import column_names
from os import path
from attack_types import *

path = "/home/adriana/dataset/"

trainSetPath = os.path.join(path, 'KDDTrain+.txt')
file = open(trainSetPath, 'r')
trainSet = pd.read_csv(file,  names = column_names.colNames)
file.close()

trainSet = attack_types_mapping(trainSet)
dos_set = trainSet[trainSet['label'] == 'Dos']
probe_set = trainSet[trainSet['label'] == 'Probe']
U2R_set = trainSet[trainSet['label'] == 'U2R']
R2L_set = trainSet[trainSet['label'] == 'R2L']
normal_set = trainSet[trainSet['label'] == 'normal']

dos_file = 'dos_dataset.csv'
probe_file = 'probe_dataset.csv'
U2R_file = 'U2R_dataset.csv'
R2L_file = 'R2L_dataset.csv'
normal_file = 'normal_dataset.csv'

dos_set.to_csv(dos_file, index=False)
probe_set.to_csv(probe_file, index=False)
U2R_set.to_csv(U2R_file, index=False)
R2L_set.to_csv(R2L_file, index=False)
normal_set.to_csv(normal_file, index=False)
