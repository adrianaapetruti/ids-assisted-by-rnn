import pandas as pd
from preprocessing_functions import *
from data_preprocessing import *
from tensorflow.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import f1_score, classification_report
from create_plot import *
from attack_types import *
from dos_data_generator import generate_dos_synthetic_data
from probe_data_generator import generate_probe_synthetic_data
from u2r_data_generator import generate_u2r_synthetic_data
from r2l_data_generator import generate_r2l_synthetic_data
from normal_data_generator import generate_normal_synthetic_data

path = "/home/adriana/dataset/"

generated_dos_set = generate_dos_synthetic_data(500)
generated_probe_set = generate_probe_synthetic_data(100)
generated_u2r_set = generate_u2r_synthetic_data(100)
generated_r2l_set = generate_r2l_synthetic_data(100)
generated_normal_set = generate_normal_synthetic_data(700)
generated_set = pd.concat([generated_dos_set, generated_probe_set, 
                           generated_u2r_set, generated_r2l_set, generated_normal_set], 
                           ignore_index=True)
print(generated_set.head(10))

distribution(generated_set).savefig("generated_set_attack_types_distribution.png")

X_fullSet, y_fullSet, label_count = data_preprocessing(generated_set)
X_fullSet = reshape_input(X_fullSet)

model_lstm = load_model('lstm.h5')
model_lstm.summary()

model_gru = load_model('gru.h5')
model_gru.summary()

def flatten(seq):
    flat_list = []
    for item in seq:
        if isinstance(item, (list, np.ndarray)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

X_fullSet = [flatten(seq) for seq in X_fullSet]
X_fullSet = [np.asarray(seq, dtype=np.float32) for seq in X_fullSet]
X_fullSet_padded = pad_sequences(X_fullSet, maxlen=122, dtype='float32', padding='post')
X_fullSet_padded = np.array(X_fullSet_padded, dtype='float32')
X_fullSet_reshaped = np.expand_dims(X_fullSet_padded, axis=1)

results_lstm = model_lstm.evaluate(X_fullSet_reshaped, y_fullSet, verbose=1)
print(f'Test results LSTM - Loss: {results_lstm[0]} - Accuracy: {results_lstm[1]*100}%')

results_gru = model_gru.evaluate(X_fullSet_reshaped, y_fullSet, verbose=1)
print(f'Test results GRU - Loss: {results_gru[0]} - Accuracy: {results_gru[1]*100}%')

y_pred = model_lstm.predict(X_fullSet_reshaped)
y_pred_labels_lstm = np.argmax(y_pred, axis=1)
y_test_labels_lstm = np.argmax(y_fullSet, axis=1)

y_pred = model_gru.predict(X_fullSet_reshaped)
y_pred_labels_gru = np.argmax(y_pred, axis=1)
y_test_labels_gru = np.argmax(y_fullSet, axis=1)

conf_matrix(y_test_labels_lstm, y_pred_labels_lstm).savefig('generated_set_confusion_matrix__lstm.png')

conf_matrix(y_test_labels_gru, y_pred_labels_gru).savefig('generated_set_confusion_matrix_gru.png')

f1_lstm = f1_score(y_test_labels_lstm, y_pred_labels_lstm, average='macro')
print("F1 Score LSTM:", f1_lstm)

f1_gru = f1_score(y_test_labels_gru, y_pred_labels_gru, average='macro')
print("F1 Score GRU:", f1_gru)

class_report_lstm = classification_report(y_test_labels_lstm, y_pred_labels_lstm, target_names=['DoS', 'Probe', 'U2R', 'R2L', 'Normal'])
print("Classification Report LSTM:\n", class_report_lstm)

class_report_gru = classification_report(y_test_labels_gru, y_pred_labels_gru, target_names=['DoS', 'Probe', 'U2R', 'R2L', 'Normal'])
print("Classification Report GRU:\n", class_report_gru)

