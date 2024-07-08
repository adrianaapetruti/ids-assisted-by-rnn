from keras.layers import Dense, LSTM, Flatten, Dropout 
from keras.models import Sequential 

def lstm_model_initialization(input_shape):
    model = Sequential()
    model.add(LSTM(64,return_sequences=True,input_shape = input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(64,return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(64,return_sequences=True))
    model.add(Flatten())
    model.add(Dense(units=50))
    model.add(Dense(units=5,activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
