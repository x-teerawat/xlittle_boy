from _libs import *
from split_train_and_test_data import split_train_and_test_data
from normalize_data import normalize_data
from form_data import form_data

def test_model(self):
    ### Determine train data
    self.selected_test_data = self.test_data[self.test_data.index>=self.start_test_date].copy()
    self.selected_test_data = self.selected

    print(tabulate(self.selected_test_data, self.selected_test_data.columns))
    print(f"len(self.selected_test_data): {len(self.selected_test_data)}")

    # for i in range(self.n_lags, len(self.selected_test_data)):
    #     print(i)
    #     if i == self.n_lags:
    #         _selected_test_data = self.selected_test_data.iloc[-self.n_lags+i+1:i+1] # +1: Because counting itself
    #         print(tabulate(_selected_test_data, _selected_test_data.columns))
    #         print(len(_selected_test_data))

    #     ### Convert DataFrame to array
    #     self.arr_selected_test_data = np.array(_selected_test_data)
    #     print(f"self.arr_selected_test_data: {self.arr_selected_test_data}")

    #     ### Normalization
    #     normalize_data(self, self.arr_selected_test_data, "testing")
    
        # ### Form data
        # form_data(self, self.arr_selected_test_data, self.n_lags, self.n_prediction_periods, self.PredictionType)

    # ### Prediction
    # self.predicted_values = self.model.predict(self.x)
    # if self.IsNormalization:
    #     self.predicted_values = self.list_scalers[self.prediction_column_nth].inverse_transform(self.predicted_values)