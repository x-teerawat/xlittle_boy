import sys
sys.path.insert(0, "../templates")
from _libs import *

def form_data(self):
    n_depths = self.arr_selected_train_data.shape[0] - self.n_lags - self.n_prediction_periods + 1
    n_rows = self.n_lags
    n_cols = self.arr_selected_train_data.shape[1]
    new_shape = (n_depths, n_rows, n_cols)
    assert n_depths >= 1, "n_depths < 1 -> Can't build the model"

    ### Split self.x and self.y
    _bytes = 8 # For dtype int64 and float64
    # self.prediction_column_nth = self.selected_train_data.columns.get_loc(self.ListPredictionType)
    self.prediction_column_nth = self.selected_train_data.columns.get_loc(self.PredictionType)
    self.x = as_strided(self.arr_selected_train_data, strides=(1*_bytes, 1*_bytes, self.arr_selected_train_data.shape[0]*_bytes), shape=new_shape)
    self.y = self.arr_selected_train_data[self.n_lags+self.n_prediction_periods-1:, self.prediction_column_nth].reshape(-1, 1)
    
    # print("Before cross validation")
    # print(f"self.x: \n{self.x}")
    # print(f"self.x.shape: {self.x.shape}")
    # print(f"self.y: \n{self.y}")
    # print(f"self.y.shape: {self.y.shape}") 
    
    