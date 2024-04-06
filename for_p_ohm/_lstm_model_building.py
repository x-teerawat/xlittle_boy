from _libs import *

def create_dataset(dataset, target, look_back=5):
    x,y =[],[]
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back),:]                                
        x.append(a)
        y.append(target[i+look_back, 0])
    return np.array(x), np.array(y)

def _lstm_model_building():
    ### Read
    df= pd.read_csv('AMD_20240102_2024_02_21_2minute')
    df.drop(columns={'vwap', 'volume'}, inplace=True)
    # print(df)

    ### Normalize
    sc_open = MinMaxScaler(feature_range=(0,1))
    sc_high = MinMaxScaler(feature_range=(0,1))
    sc_low = MinMaxScaler(feature_range=(0,1))
    sc_close = MinMaxScaler(feature_range=(0,1))

    sc_open_fit = sc_open.fit_transform(df['open'].values.reshape(-1,1))
    sc_high_fit = sc_high.fit_transform(df['high'].values.reshape(-1,1))
    sc_low_fit = sc_low.fit_transform(df['low'].values.reshape(-1,1))
    sc_close_fit = sc_close.fit_transform(df['close'].values.reshape(-1,1))

    ### Generate x and y
    look_back = 10
    x_open,_ = create_dataset(sc_open_fit,sc_open_fit,look_back)
    x_high,_ = create_dataset(sc_high_fit,sc_high_fit,look_back)
    x_low,_=create_dataset(sc_low_fit,sc_low_fit, look_back )
    x_close,_ = create_dataset(sc_close_fit, sc_close_fit,look_back)

    x_final= np.dstack((x_open,x_high,x_low,x_close))

    _,y_high = create_dataset(sc_high_fit,sc_high_fit, look_back)
    _,y_low = create_dataset(sc_low_fit,sc_low_fit,look_back)

    ### Split data
    train_size = int(len(x_final))
    train_size_80 = int(len(x_final)*0.8)

    x_train = x_final[0:train_size_80]
    # x_train = x_final[0:train_size_80-1]
    x_test = x_final[train_size_80:len(x_final)]
    y_high_train=y_high[0:train_size_80]
    # y_high_train=y_high[1:train_size_80]
    y_high_test=y_high[train_size_80:len(y_high)]
    y_low_train=y_low[0:train_size_80]
    y_low_test=y_low[0:train_size_80:len(y_low)]

    ### Build model
    input_layer = Input(shape=(look_back, 4))
    lstm1 = LSTM(units=10, return_sequences=True)(input_layer)
    dropout1=Dropout(0.2)(lstm1)
    lstm2 = LSTM(units=10)(dropout1)
    dropout2 = Dropout(0.2)(lstm2)
    output_layer = Dense(1)(dropout2)

    model_high_no_shift = Model(inputs=input_layer, outputs=output_layer)
    model_high_no_shift.compile(loss='mean_squared_error', optimizer='adam')

    # list_epochs = [5*i for i in range(1, 6)]
    # list_batch_sizes = [2**i for i in range(6)]
    # list_validation_splits = [float(f"0.{i}") for i in range(1, 6)]
    # list_thresholds = [float(f"0.{i}") for i in range(1, 6)]

    list_epochs = [2*i for i in range(1, 6)]
    list_batch_sizes = [5**i for i in range(1, 4)]
    list_validation_splits = [float(f"0.{i}") for i in range(1, 4)]
    list_thresholds = [float(f"0.{i}") for i in range(1, 4)]

    # list_params = []
    # list_win_rates = []
    for epochs in list_epochs:
        for batch_size in list_batch_sizes:
            for validation_split in list_validation_splits:
                for threshold in list_thresholds:
                    IsFoundModel = False

                    his_high = model_high_no_shift.fit(x_train, y_high_train, epochs=epochs, batch_size=batch_size, verbose=1, validation_split=validation_split)

                    ### Predict
                    predicted_high_price = model_high_no_shift.predict(x_test)

                    ### Inverse transform
                    inversed_y_high_test = sc_high.inverse_transform(y_high_test.reshape(-1, 1))
                    # inversed_y_high_test = sc_high.inverse_transform(y_high_test[1:].reshape(-1, 1))
                    inversed_predicted_high_price = sc_high.inverse_transform(predicted_high_price)
                    result_df = pd.DataFrame({
                        'actual': inversed_y_high_test[:, 0],
                        'prediction': inversed_predicted_high_price[:, 0],
                    })
                    result_df['diff_pct_change_between_actual_and_prediction'] = abs((result_df.actual - result_df.prediction) / result_df.prediction * 100)

                    ### Compute win rate
                    status = [1 if i<=threshold else 0 for i in result_df.diff_pct_change_between_actual_and_prediction]
                    status_df = pd.DataFrame(status, columns=['status'])

                    try:
                        win_rate = status_df.value_counts()[1]/len(status_df)*100
                    except Exception as e:
                        win_rate = 0

                    ### Update
                    result_df['win_rate'] = win_rate

                    params = f"epochs_{epochs}__batch_size_{batch_size}__validation_split_{validation_split}__threshold_{threshold}"
                    print(f"win_rate: {win_rate}")
                    print(f"params: {params}")

                    if win_rate >= 30:
                        IsFoundModel = True
                        # list_params.append(params)
                        # list_win_rates.append(win_rate)

                        ### Save
                        model_high_no_shift.save(f'{params}.keras')

                        break

                    print(f"IsFoundModel: {IsFoundModel}")

                if IsFoundModel == True:
                    break
            if IsFoundModel == True:
                break
        if IsFoundModel == True:
            break
                    
if __name__ == "__main__":
    _lstm_model_building()


    # max_win_rate_idx = np.argmax(list_win_rates)
    # best_params = list_params[max_win_rate_idx]
