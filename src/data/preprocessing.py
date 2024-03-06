import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def preprocessing(data_path):
    gstock_data = pd.read_csv(data_path)
    # print("current:: " , gstock_data.fillna.sum())


    gstock_data.columns = gstock_data.columns.str.lower()
    gstock_data = gstock_data[['date', 'open', 'close']]

    gstock_data['date'] = pd.to_datetime(gstock_data['date'].apply(lambda x: x.split(' ')[0]))
    gstock_data.set_index('date', inplace=True)
    
    return gstock_data

def visualize_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['open'], label='Open', color='green')
    plt.plot(data['close'], label='Close', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('GOOG Stock Prices')
    plt.legend()
    plt.show()


def scale_data(data):
    scaler = MinMaxScaler()
    processed_data = scaler.fit_transform(data)
    return processed_data
    

def splitting_data(processed_data):
    train_data, test_data = processed_data[:int(len(processed_data) * 0.8)], processed_data[int(len(processed_data) * 0.8):]
    return train_data, test_data

    


