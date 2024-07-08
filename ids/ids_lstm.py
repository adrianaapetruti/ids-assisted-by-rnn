import pandas as pd
import os
from os import path
from sklearn.model_selection import train_test_split 
import column_names
from create_plot import *
from preprocessing_functions import *
from data_preprocessing import *
from lstm_model import lstm_model_initialization
import warnings
warnings.filterwarnings("ignore")

path = "/home/adriana/dataset/"

trainSetPath = os.path.join(path, 'KDDTrain+.txt')
file = open(trainSetPath, 'r')
trainSet = pd.read_csv(file,  names = column_names.colNames)
file.close()

labels = trainSet['label']

X_fullSet, y_fullSet, label_count = data_preprocessing(trainSet)
X_train, X_test, y_train, y_test = train_test_split(X_fullSet, y_fullSet, test_size=0.20, random_state=42)

X_train = reshape_input(X_train)
X_test = reshape_input(X_test)

print(X_train.shape,'\n',X_test.shape)

input_shape = (X_train.shape[1], X_train.shape[2])
model = lstm_model_initialization(input_shape)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
history = model.fit(X_train.astype(float), y_train, epochs=100, batch_size=5000, validation_split=0.2)

model.save('lstm.h5')
model_performance(history).savefig("lstm_model_performance.png")

results = model.evaluate(X_test.astype(float), y_test, verbose=1)
print(f'Test results - Loss: {results[0]} - Accuracy: {results[1]*100}%')

