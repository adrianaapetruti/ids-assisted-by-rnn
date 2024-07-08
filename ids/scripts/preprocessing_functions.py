import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, LabelBinarizer

def standardization(set, col):
    for i in col:
        arr = set[i]
        arr = np.array(arr)
        set[i] = StandardScaler().fit_transform(arr.reshape(len(arr),1))
    return set

def label_encoding(set, label):
    le = preprocessing.LabelEncoder()
    enc_label = label.apply(le.fit_transform)
    set['intrusion'] = enc_label
    set.drop(labels = ['label'], axis=1, inplace=True)
    return set

def one_hot_encoding(set, col):
    set = pd.get_dummies(set, columns=col, prefix="", prefix_sep="")
    return set

def binarize_labels(set):
    set = LabelBinarizer().fit_transform(set)
    return set

def reshape_input(set):
    set = np.reshape(set, (set.shape[0], 1, set.shape[1]))
    return set
