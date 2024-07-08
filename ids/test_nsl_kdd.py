import pandas as pd
import os
from os import path
import warnings
import absl.logging
warnings.filterwarnings("ignore")
absl.logging.set_verbosity(absl.logging.ERROR)

from sklearn.model_selection import train_test_split
import column_names
from preprocessing_functions import *
from data_preprocessing import *
from tensorflow.keras.models import load_model
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from create_plot import *
from attack_types import *

path = "/home/adriana/dataset/"

trainSetPath = os.path.join(path, 'KDDTrain+.txt')
file = open(trainSetPath, 'r')
trainSet = pd.read_csv(file,  names = column_names.colNames)
print(trainSet.head(10))
file.close()

testSetPath = os.path.join(path, 'KDDTest+.txt')
file = open(testSetPath, 'r')
testSet = pd.read_csv(file,  names = column_names.colNames)
file.close()

distribution(trainSet).savefig("train_set_attack_types_distribution.png")
distribution(testSet).savefig("test_set_attack_types_distribution.png")

fullSet = pd.concat([trainSet, testSet], ignore_index=True)

X_fullSet, y_fullSet, label_count = data_preprocessing(fullSet)
X_train, X_test, y_train, y_test = train_test_split(X_fullSet, y_fullSet, test_size=0.20, random_state=42)

normal_count = (label_count['normal'] * 0.2).astype(int)
DoS_count = (label_count['Dos'] * 0.2).astype(int)
Probe_count = (label_count['Probe'] * 0.2).astype(int)
U2R_count = (label_count['U2R'] * 0.2).astype(int) 
R2L_count = (label_count['R2L'] * 0.2).astype(int)

X_train = reshape_input(X_train)
X_test = reshape_input(X_test)

lstm_model = load_model('lstm.h5')
lstm_model.summary()

gru_model = load_model('gru.h5')
gru_model.summary()

results_lstm = lstm_model.evaluate(X_test.astype(float), y_test, verbose=1)
print(f'Test results lstm - Loss: {results_lstm[0]} - Accuracy: {results_lstm[1]*100}%')

results_gru = gru_model.evaluate(X_test.astype(float), y_test, verbose=1)
print(f'Test results gru - Loss: {results_gru[0]} - Accuracy: {results_gru[1]*100}%')

y_pred_lstm = lstm_model.predict(X_test.astype(float))
y_pred_labels_lstm = np.argmax(y_pred_lstm, axis=1)
y_test_labels_lstm = np.argmax(y_test, axis=1)

conf_matrix(y_test_labels_lstm, y_pred_labels_lstm).savefig('lstm_confusion_matrix.png')

y_pred_gru = gru_model.predict(X_test.astype(float))
y_pred_labels_gru = np.argmax(y_pred_lstm, axis=1)
y_test_labels_gru = np.argmax(y_test, axis=1)

conf_matrix(y_test_labels_gru, y_pred_labels_gru).savefig('gru_confusion_matrix.png')

f1_lstm = f1_score(y_test_labels_lstm, y_pred_labels_lstm, average='macro')
print("F1 Score LSTM model:", f1_lstm)

f1_gru = f1_score(y_test_labels_gru, y_pred_labels_gru, average='macro')
print("F1 Score GRU model:", f1_gru)

class_report_lstm = classification_report(y_test_labels_lstm, y_pred_labels_lstm, 
                target_names = ["DOS","Probe","R2L","U2R", "Normal"])
print("Classification Report LSTM model:\n", class_report_lstm)

class_report_gru = classification_report(y_test_labels_lstm, y_pred_labels_lstm, 
                target_names = ["DOS","Probe","R2L","U2R", "Normal"])
print("Classification Report GRU model:\n", class_report_gru)
