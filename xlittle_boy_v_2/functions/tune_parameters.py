# from save_model_weights import save_model_weights
from form_data import form_data
from normalize_data import normalize_data
from cross_validation import cross_validation
from split_train_and_validation_data import split_train_and_validation_data
from evaluate_model import evaluate_model
from _build_models import _build_models

import sys
sys.path.insert(0, "../templates")
from _libs import *

def tune_parameters(self):
    for self.model_name in self.list_model_names:
        for self.PredictionType in self.ListPredictionType:
            for self.n_prediction_periods in self.list_n_prediction_periods:
                for self.n_lags in self.list_n_lags:
                    for self.IsNormalization in self.ListIsNormalization:
                        for self.IsCrossValidation in self.ListIsCrossValidation:
                            for self.n_validation_size in self.list_n_validation_sizes:
                                ### Determine train data
                                self.selected_train_data = self.train_data[['open', 'high', 'low', 'close']].copy()
                                # self.selected_train_data = self.selected_train_data.tail(20)

                                ### Convert DataFrame to array
                                self.arr_selected_train_data = np.array(self.selected_train_data)
                                # print(f"self.arr_selected_train_data.shape: {self.arr_selected_train_data.shape}")
                                # print(f"self.arr_selected_train_data: \n{self.arr_selected_train_data}")
                                
                                ### Normalization
                                normalize_data(self)

                                ### Form data
                                form_data(self)

                                ### Cross validation
                                cross_validation(self)

                                ### Split train and validation data
                                split_train_and_validation_data(self)

                                for self.n_epochs in self.list_n_epochs:
                                    for self.n_batch_size in self.list_n_batch_sizes:
                                        self.params = f"model_name_{self.model_name}__PredictionType_{self.PredictionType}__n_prediction_periods_{self.n_prediction_periods}__n_lags_{self.n_lags}__IsCrossValidation_{self.IsCrossValidation}__n_validation_size_{self.n_validation_size}__n_epochs_{self.n_epochs}__n_batch_size_{self.n_batch_size}"
                                        print(f"params: \n{self.params}")

                                        ### Build a model
                                        _build_models(self)    

                                        ### Prediction
                                        self.predicted_values = self.model.predict(self.x_valid)
                                        if self.IsNormalization:
                                            self.predicted_values = self.list_scalers[self.prediction_column_nth].inverse_transform(self.predicted_values)

                                        ### Evaluate model
                                        evaluate_model(self)
                                        print()

                                        if self.win_rate >= self.win_rate_treshold:
                                            if self.IsSaveModel:
                                                self.model.save(f"{self.params}")
                                            break
                                    if self.win_rate >= self.win_rate_treshold:
                                        break
                                if self.win_rate >= self.win_rate_treshold:
                                    break
                            if self.win_rate >= self.win_rate_treshold:
                                break
                        if self.win_rate >= self.win_rate_treshold:
                            break
                    if self.win_rate >= self.win_rate_treshold:
                        break
                if self.win_rate >= self.win_rate_treshold:
                    break
            if self.win_rate >= self.win_rate_treshold:
                break
        if self.win_rate >= self.win_rate_treshold:
            break
        
                            