from _libs import *
import time

def create_dataset(dataset, target, look_back=5):
    x,y =[],[]
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back),:]                                
        x.append(a)
        y.append(target[i+look_back, 0])
    return np.array(x), np.array(y)

def _lstm_model_prediction():
    train_data= pd.read_csv('AMD_20240102_2024_02_21_2minute')
    train_data.drop(columns={'vwap', 'volume'}, inplace=True)
    test_data= pd.read_csv('AMD_20240222_2024_02_29_2minute')
    test_data.drop(columns={'vwap', 'volume'}, inplace=True)

    """
        Note: ชื่อไฟล์จะต้องตรงกับ _lstm_model_building.py และ _lstm_model_building.py
    """
    model_file_name = 'epochs_2__batch_size_5__validation_split_0.3__threshold_0.3.keras' 

    look_back = 10
    threshold = 0.3

    sc_open = MinMaxScaler(feature_range=(0,1))
    sc_high = MinMaxScaler(feature_range=(0,1))
    sc_low = MinMaxScaler(feature_range=(0,1))
    sc_close=MinMaxScaler(feature_range=(0,1))

    df = pd.concat([train_data,test_data])
    df.reset_index(inplace=True, drop=True)
    model = load_model(model_file_name)
    list_date = []
    new_win_rate_data = pd.DataFrame()

    result_df = df.iloc[len(train_data)-look_back+1:len(train_data)].copy() # len(train_data): previous test data follow by look back
    for i, j in df.iloc[len(train_data):].iterrows():
    # for i, j in df.iloc[len(train_data):len(train_data)].iterrows():

        fitting_data = df.iloc[:i+1].copy() # For max-min scaling
        selected_df = df.iloc[i-look_back+1:i+1].copy()
        
        sc_open_fit = sc_open.fit(fitting_data['open'].values.reshape(-1,1))
        sc_high_fit = sc_high.fit(fitting_data['high'].values.reshape(-1,1))
        sc_low_fit = sc_low.fit(fitting_data['low'].values.reshape(-1,1))
        sc_close_fit = sc_close.fit(fitting_data['close'].values.reshape(-1,1))

        sc_open_transform = sc_open_fit.transform(selected_df['open'].values.reshape(-1,1))
        sc_high_transform = sc_high_fit.transform(selected_df['high'].values.reshape(-1,1))
        sc_low_transform = sc_low_fit.transform(selected_df['low'].values.reshape(-1,1))
        sc_close_transform = sc_close_fit.transform(selected_df['close'].values.reshape(-1,1))

        x_test = np.dstack((
            sc_open_transform,
            sc_high_transform,
            sc_low_transform,
            sc_close_transform,
        ))
        
        x_test = x_test.reshape(1, look_back, 4)

        predicted_high_price = model.predict(x_test, verbose=0)
        inversed_y_high_test = sc_high_fit.inverse_transform(predicted_high_price)[0][0]

        ### Update result data
        # result_df = pd.concat([result_df, selected_df.tail(1)])
        result_df.loc[i, ['timestamp', 'prediction']] = [selected_df.iloc[-1].timestamp, inversed_y_high_test]
        # result_df.loc[i, 'timestamp'] = pd.to_datetime(selected_df.loc[i, 'timestamp'])+ relativedelta(minutes=2)
        # result_df.loc[i, ['prediction_value']] = [inversed_y_high_test]
        result_df.loc[i-1, ['open', 'high', 'low', 'close']] = selected_df.tail(2)[['open', 'high', 'low', 'close']].values[0]
        result_df['difference_between_actual_and_prediction'] = abs((result_df.high - result_df.prediction) / result_df.prediction * 100)
        result_df['win_loss'] = [1 if i<=threshold else 0 for i in result_df.difference_between_actual_and_prediction]
        print(result_df)
        time.sleep(1)
        current_date = pd.to_datetime(j.timestamp).strftime("%Y-%m-%d")
        list_date.append(current_date)

        try:
            previous_date = list_date[-2]

            if current_date == previous_date:
                result_df_without_missing_value = result_df[~result_df.difference_between_actual_and_prediction.isna()].copy()
                result_df_without_missing_value = result_df_without_missing_value.tail(1)
                new_win_rate_data = pd.concat([new_win_rate_data, result_df_without_missing_value])
            else:
                print(new_win_rate_data)
                win_rate = new_win_rate_data.win_loss.sum() / len(new_win_rate_data) * 100

                """
                    Note: ถ้า win_rate < set point ให้ Tricker "_lstm_model_retaining.py" file
                """
                new_win_rate_data = pd.DataFrame({
                    "date": [previous_date],
                    "win_rate": [win_rate]
                })
                print(new_win_rate_data)
                win_rate_data = pd.read_csv("win_rate_data.csv", index_col=0)
                win_rate_data = pd.concat([win_rate_data, new_win_rate_data])
                win_rate_data.to_csv("win_rate_data.csv")

                new_win_rate_data = pd.DataFrame() # Reset DataFrame

        except:
            pass

if __name__ == "__main__":
    _lstm_model_prediction()