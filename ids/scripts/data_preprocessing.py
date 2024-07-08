import pandas as pd
from attack_types import attack_types_mapping
from preprocessing_functions import *
import warnings
warnings.filterwarnings("ignore")
from create_plot import *

def data_preprocessing(set):
    set = attack_types_mapping(set)
    set.drop(['difficulty'], axis=1, inplace=True)
    distribution(set).savefig("attack_types_distribution.png")

    label_count = set['label'].value_counts()

    set.T

    numeric_col = set.select_dtypes(include='number').columns
    set = standardization(set, numeric_col)

    label = pd.DataFrame(set.label)
    set = label_encoding(set, label)

    cat_columns = ['protocol_type', 'service', 'flag']
    set = one_hot_encoding(set, cat_columns)

    y_set = set['intrusion']
    X_set = set.drop(labels = ['intrusion'], axis=1)

    y_set = binarize_labels(y_set)

    y_set = np.array(y_set)
    X_set = np.array(X_set)

    return X_set, y_set, label_count
