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
        list_n_atr,
        list_n_ema,
        list_n_macd,
        list_n_rsi,
        list_n_tr,
        ListPredictionTypes,
        list_model_names,
        list_n_prediction_periods,
        list_n_lags,
        ListIsNormalization,
        ListIsCrossValidations,
        list_n_validation_sizes,
        list_n_epochs,
        list_n_batch_sizes,
        threshold_between_actual_and_predicted_values,
        win_rate_treshold,
        IsSaveData,
        IsSaveModel,
        IsSaveScaler
    ):
        self.stock_name = stock_name
        self.start_test_date = start_test_date
        self.n_train_periods = n_train_periods
        self.n_test_periods = n_test_periods
        self.n_multiplier = n_multiplier
        self.timespan = timespan
        self.list_n_atr = list_n_atr
        self.list_n_ema = list_n_ema
        self.list_n_macd = list_n_macd
        self.list_n_rsi = list_n_rsi
        self.list_n_tr = list_n_tr
        self.ListPredictionTypes = ListPredictionTypes
        self.list_model_names = list_model_names
        self.list_n_prediction_periods = list_n_prediction_periods
        self.list_n_lags = list_n_lags
        self.ListIsNormalization = ListIsNormalization
        self.ListIsCrossValidations = ListIsCrossValidations
        self.list_n_validation_sizes = list_n_validation_sizes
        self.list_n_epochs = list_n_epochs
        self.list_n_batch_sizes = list_n_batch_sizes
        self.threshold_between_actual_and_predicted_values = threshold_between_actual_and_predicted_values
        self.win_rate_treshold = win_rate_treshold
        
        self.IsSaveData = IsSaveData
        self.IsSaveModel = IsSaveModel
        self.IsSaveScaler = IsSaveScaler

        self.start_train_date = pd.to_datetime(self.start_test_date) - relativedelta(days=self.n_train_periods)
        # self.start_train_date = self.start_train_date.tz_localize('US/Eastern')
        self.end_train_date = pd.to_datetime(self.start_test_date) - relativedelta(days=1)
        self.end_test_date = pd.to_datetime(self.start_test_date)

        self.file_name = f"stock_name_{self.stock_name}__start_test_date_{self.start_test_date}__n_train_periods_{self.n_train_periods}__n_test_periods_{self.n_test_periods}__n_multiplier_{self.n_multiplier}__timespan_{self.timespan}"

    def run(self):
        ### Get data
        if self.IsSaveData:
            get_data(self)
            self.data.to_csv(f"data/{self.file_name}.csv")
        else:
            self.data = pd.read_csv(f"data/{self.file_name}.csv", index_col=0)
    
        ### Prepare data
        prepare_data(self)
        # print(tabulate(self.prepared_data, self.prepared_data.columns))
        
        ### Clean data
        self.cleaned_data = clean_data(self, self.prepared_data)

        ### Generate indicators
        # indicator_atr(self)
        # indicator_banker_retail(self)
        # indicator_ema(self)
        # indicator_macd(self)
        # indicator_rsi(self)
        # indicator_tr(self)

        ### Search
        # search_ema_crossover_and_crossunder(self)

        ### Determine data
        determine_data(self)

        ### Parameter tuning
        tune_hyperparameters(self)

        ### Test models
        # print(f"self.list_low_and_high_scalers['high']: {self.list_low_and_high_scalers['high']}")
        # print(f"type(self.list_low_and_high_scalers['high']): {type(self.list_low_and_high_scalers['high'])}")
        test_model(self)


        ### Transfer learning
        # transfer_learning(self)
