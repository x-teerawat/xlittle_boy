import sys
sys.path.insert(0, "../templates")
from _libs import *

def normalize_data(self):
    if self.IsNormalization:
        ### Normalized
        n_cols = self.arr_selected_train_data.shape[1]
        scaler = MinMaxScaler(feature_range=(0,1))
        self.list_scalers = []

        for col_nth in range(n_cols):
            _scaler = scaler.fit(self.arr_selected_train_data[:, col_nth].reshape(-1, 1))
            self.list_scalers.append(_scaler)
            scaled_values = _scaler.transform(self.arr_selected_train_data[:, col_nth].reshape(-1, 1))
            self.arr_selected_train_data[:, col_nth] = scaled_values.flatten()
            
        # print("self.arr_selected_train_data")
        # print(self.arr_selected_train_data)