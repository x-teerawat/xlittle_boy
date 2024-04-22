import sys
sys.path.insert(0, "../templates")
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
                self.list_scalers.append(_scaler)
                scaled_values = _scaler.transform(data[:, col_nth].reshape(-1, 1))
                data[:, col_nth] = scaled_values.flatten()
                
            ### For checking data similarity
            # print(f"data==self.arr_selected_train_data: {data==self.arr_selected_train_data}")
        elif processing_type == 'testing':
            for col_nth in range(self.n_cols):
                print(f"data[-1, col_nth]: {data[-1, col_nth]}")
                # _scaler = self.list_scalers[col_nth].fit(data[-1, col_nth].reshape(-1, 1))

                # scaled_values = _scaler.transform(data[:, col_nth].reshape(-1, 1))
                # data[:, col_nth] = scaled_values.flatten()
