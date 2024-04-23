from _libs import *
from split_train_and_test_data import split_train_and_test_data
from normalize_data import normalize_data
from form_data import form_data

def test_model(self):
    ### Determine test data
    self.selected_test_data = self.test_data[self.test_data.index>=self.start_test_date].copy()
    list_model_in_use_file_names = os.listdir('../models_in_use')
    print(f"list_model_in_use_file_names: {list_model_in_use_file_names}")

    for test_date in self.selected_test_data.index:
        for model_in_use_file_name in list_model_in_use_file_names:
            all_params = model_in_use_file_name.split('__')[1:]
            self.PredictionType = all_params[0].split('_')[-1]
            n_prediction_periods = int(all_params[1].split('_')[-1])
            n_lags = int(all_params[2].split('_')[-1])
            IsCrossValidation = bool(all_params[3].split('_')[-1])
            n_validation_size = float(all_params[4].split('_')[-1])
            n_epochs = int(all_params[5].split('_')[-1])
            n_batch_size = int(all_params[6].split('_')[-1])

            # print(f"model_in_use_file_name: {model_in_use_file_name}")
            # print(f"all_params: {all_params}")
            # print(f"self.PredictionType: {self.PredictionType}")
            # print(f"n_prediction_periods: {n_prediction_periods}")
            # print(f"n_lags: {n_lags}")
            # print(f"IsCrossValidation: {IsCrossValidation}")
            # print(f"n_validation_size: {n_validation_size}")
            # print(f"n_epochs: {n_epochs}")
            # print(f"n_batch_size: {n_batch_size}")
            # print()

             ### Determine train data
            self.selected_train_data = self.train_data[['open', 'high', 'low', 'close']].copy()

            ### Convert DataFrame to array
            self.arr_selected_train_data = np.array(self.selected_train_data)

            ### Determine test data
            _test_data = self.test_data[self.test_data.index<=test_date].tail(n_lags)
            _selected_test_data = _test_data[['open', 'high', 'low', 'close']].copy()

            print(tabulate(_selected_test_data, _selected_test_data.columns))

            ### Convert DataFrame to array
            self.arr_selected_test_data = np.array(_selected_test_data)
            print("B")
            print(f"self.arr_selected_test_data: {self.arr_selected_test_data}")


            ### Normalization
            normalize_data(self, self.arr_selected_test_data, "testing")
            print("A")
            print(f"self.arr_selected_test_data: {self.arr_selected_test_data}")
            print("-"*100)

            # ### Prediction
            # self.predicted_values = self.model.predict(self.x)
            # if self.IsNormalization:
            #     self.predicted_values = self.list_scalers[self.prediction_column_nth].inverse_transform(self.predicted_values)