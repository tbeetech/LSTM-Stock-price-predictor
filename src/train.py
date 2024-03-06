import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional
# from tensorflow.keras.metrics import MeanSquaredError, MeanAbsoluteError
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

    
window_size = 50

def create_sequences(data, window_size):
    
    sequences = []
    labels = []
    for i in range(len(data) - window_size):
        sequences.append(data[i:i+window_size])
        labels.append(data[i+window_size])
    
    return np.array(sequences), np.array(labels)

def train_model():

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(train_seq.shape[1], train_seq.shape[2])),
        Dropout(0.2),
        LSTM(50),
        Dropout(0.2),
        Dense(1)
    ])

    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    model.summary()

    history = model.fit(train_seq, train_label, epochs=50, batch_size=64, validation_data=(test_seq, test_label), verbose=1)
        
    return model, history
