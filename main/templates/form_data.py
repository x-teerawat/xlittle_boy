import sys
sys.path.insert(0, "../templates")
from _libs import *

def form_data(self, data, n_lags, n_prediction_periods, PredictionType):
    n_depths = data.shape[0] - n_lags - n_prediction_periods + 1
    n_rows = n_lags
    n_cols = data.shape[1]
    new_shape = (n_depths, n_rows, n_cols)
    assert n_depths >= 1, "n_depths < 1 -> Can't build the model"

    ### Split self.x and self.y
    _bytes = 8 # For dtype int64 and float64
    self.prediction_column_nth = self.cleaned_data.columns.get_loc(PredictionType)
    self.x = as_strided(data, strides=(1*_bytes, 1*_bytes, data.shape[0]*_bytes), shape=new_shape)
    self.y = data[n_lags+n_prediction_periods-1:, self.prediction_column_nth].reshape(-1, 1)
    
    # print("Before cross validation")
    # print(f"self.x: \n{self.x}")
    # print(f"self.x.shape: {self.x.shape}")
    # print(f"self.y: \n{self.y}")
    # print(f"self.y.shape: {self.y.shape}") 
    
    