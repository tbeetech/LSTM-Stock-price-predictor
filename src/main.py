from data.preprocessing import preprocessing,visualize_data,scale_data,splitting_data
from train import create_sequences,window_size

pro_data = scale_data(preprocessing('./GOOG.csv'))

train_data, test_data = splitting_data(pro_data)
train_seq, train_label = create_sequences(train_data,window_size)
test_seq, test_label = create_sequences(test_data, window_size)

print('Train Features: ', train_seq)
print('Test Features: ', test_seq)