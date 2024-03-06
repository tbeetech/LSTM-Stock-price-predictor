def evaluate():
   scaler = MinMaxScaler()
   predicted_prices = model.predict(test_seq)
   predicted_prices = scaler.inverse_transform(predicted_prices.reshape(-1, 2))
   test_prices = scaler.inverse_transform(test_label.reshape(-1, 2))
   mse = mean_squared_error(test_prices, predicted_prices)
   mae = mean_absolute_error(test_prices, predicted_prices)
    
   return mse, mae, predicted_prices, test_prices

