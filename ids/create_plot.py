import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def distribution(set):
    set['label'].value_counts().plot(kind='bar')
    plt.xlabel('Attack type')
    plt.ylabel('Count')
    return plt

def model_performance(history):
    tr_acc = history.history['accuracy']
    tr_loss = history.history['loss']
    val_acc = history.history['val_accuracy']
    val_loss = history.history['val_loss']
    index_loss = np.argmin(val_loss)
    val_lowest = val_loss[index_loss]
    index_acc = np.argmax(val_acc)
    acc_highest = val_acc[index_acc]
    Epochs = [i+1 for i in range(len(tr_acc))]
    loss_label = f'cea mai bună epocă= {str(index_loss + 1)}'
    acc_label = f'cea mai bună epocă= {str(index_acc + 1)}'

    plt.figure(figsize= (20, 8))
    plt.style.use('seaborn-v0_8-poster')

    plt.subplot(1, 2, 1)
    plt.plot(Epochs, tr_loss, 'r', label= 'Pierderea antrenării')
    plt.plot(Epochs, val_loss, 'g', label= 'Pierderea validării')
    plt.scatter(index_loss + 1, val_lowest, s= 150, c= 'blue', label= loss_label)
    plt.title('Pierderile antrenării și validării')
    plt.xlabel('Epocă')
    plt.ylabel('Pierdere')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(Epochs, tr_acc, 'r', label= 'Acuratețea antrenării')
    plt.plot(Epochs, val_acc, 'g', label= 'Acuratețea validării')
    plt.scatter(index_acc + 1 , acc_highest, s= 150, c= 'blue', label= acc_label)
    plt.title('Acuratețea antrenării și validării')
    plt.xlabel('Epocă')
    plt.ylabel('Accuratețe')
    plt.legend()

    plt.tight_layout
    return plt

def conf_matrix(test_labels, pred_labels):
    cm = confusion_matrix(test_labels, pred_labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    return plt
