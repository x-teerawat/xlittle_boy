import sys
sys.path.insert(0, "templates")
from _libs import *

def normalize_data(self, data, processing_type):
    if self.IsNormalization:
        if processing_type == 'training':
            ### Normalized
            self.n_cols = data.shape[1]
            scaler = MinMaxScaler(feature_range=(0,1))
            self.list_scalers = []

            for col_nth in range(self.n_cols):
                _scaler = scaler.fit(data[:, col_nth].reshape(-1, 1))
                scaled_values = _scaler.transform(data[:, col_nth].reshape(-1, 1))
                data[:, col_nth] = scaled_values.flatten()

                self.list_scalers.append(_scaler)

            ### For checking data similarity
            # print(f"data==self.arr_selected_train_data: {data==self.arr_selected_train_data}")

        elif processing_type == 'testing':
            scaler = self.dict_low_and_high_scalers[self.PredictionType]


            for col_nth in range(self.n_cols):
                print(f"data[-1, col_nth].reshape(-1, 1): {data[-1, col_nth].reshape(-1, 1)}")
                print(f"data[:, col_nth].reshape(-1, 1): {data[:, col_nth].reshape(-1, 1)}")

                # _scaler = scaler[col_nth].fit(data[-1, col_nth].reshape(-1, 1))
                # scaled_values = _scaler.transform(data[:, col_nth].reshape(-1, 1))

                scaled_values = scaler[col_nth].transform(data[:, col_nth].reshape(-1, 1))

                # inversed = _scaler.inverse_transform(data[:, col_nth].reshape(-1, 1))

                data[:, col_nth] = scaled_values.flatten()

                print(f"scaled_values: {scaled_values}")
                # print(f"inversed: {inversed}")


            # scaled_values = scaler[0].fit_transform(data[:, 0].reshape(-1, 1))
            # print(f"scaled_values: {scaled_values}")
            # print(f"scaled_values>1: {scaled_values>1}")
            # print(f"scaled_values<0: {scaled_values<0}")

                # _scaler = self.dict_low_and_high_scalers[self.PredictionType][col_nth].fit(data[-1, col_nth].reshape(-1, 1))
                # scaled_values = _scaler.transform(data[:, col_nth].reshape(-1, 1))
                # data[:, col_nth] = scaled_values.flatten()

