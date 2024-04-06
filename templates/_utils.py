from _libs import *
from _funcs import *

class Utils():
    def __init__(
        self,
        stock_name,
        start_test_date,
        n_train_periods,
        n_test_periods,
        n_multiplier,
        timespan,
        list_n_ema,
        list_model_names,
        ListPredictionType,
        list_n_prediction_periods,
        list_n_lags,
        ListIsNormalization,
        ListIsCrossValidation,
        list_n_validation_sizes,
        list_n_epochs,
        list_n_batch_sizes,
        threshold_between_actual_and_predicted_values,
        win_rate_treshold,
        IsSaveData,
        IsSaveModel,
    ):
        self.stock_name = stock_name
        self.start_test_date = start_test_date
        self.n_train_periods = n_train_periods
        self.n_test_periods = n_test_periods
        self.n_multiplier = n_multiplier
        self.timespan = timespan
        self.list_n_ema = list_n_ema
        self.list_model_names = list_model_names
        self.ListPredictionType = ListPredictionType
        self.list_n_prediction_periods = list_n_prediction_periods
        self.list_n_lags = list_n_lags
        self.ListIsNormalization = ListIsNormalization
        self.ListIsCrossValidation = ListIsCrossValidation
        self.list_n_validation_sizes = list_n_validation_sizes
        self.list_n_epochs = list_n_epochs
        self.list_n_batch_sizes = list_n_batch_sizes
        self.threshold_between_actual_and_predicted_values = threshold_between_actual_and_predicted_values
        self.win_rate_treshold = win_rate_treshold
        
        self.IsSaveData = IsSaveData
        self.IsSaveModel = IsSaveModel

        self.start_train_date = pd.to_datetime(self.start_test_date) - relativedelta(days=self.n_train_periods)
        self.end_train_date = pd.to_datetime(self.start_test_date) - relativedelta(days=1)
        self.end_test_date = pd.to_datetime(self.start_test_date) + relativedelta(days=self.n_test_periods)

        self.file_name = f"stock_name_{self.stock_name}__start_test_date_{self.start_test_date}__n_train_periods_{self.n_train_periods}__n_test_periods_{self.n_test_periods}__n_multiplier_{self.n_multiplier}__timespan_{self.timespan}"

    def run(self):
        ### Get data
        if self.IsSaveData:
            get_data(self)
            self.data.to_csv(f"../data/{self.file_name}.csv")
        else:
            self.data = pd.read_csv(f"../data/{self.file_name}.csv", index_col=0)
    
        ### Prepare data
        prepare_data(self)
        # print(tabulate(self.prepared_data, self.prepared_data.columns))

        ### Generate indicators
        # indicator_ema(self)
        # print(tabulate(self.prepared_data, self.prepared_data.columns))

        ### Split train and test data
        split_train_and_test_data(self)
        # print(f"Train date: \n{self.train_data.index[0]} - {self.train_data.index[-1]}")
        # print(f"Test date: \n{self.test_data.index[0]} - {self.test_data.index[-1]}")
        # print("train_data")
        # print(tabulate(self.train_data, self.train_data.columns))
        # print("test_data")
        # print(tabulate(self.test_data, self.test_data.columns))

        ### Parameter tuning
        tune_parameters(self)


        ### Transfer learning
        # transfer_learning(self)

        # a()
        # print(1)
