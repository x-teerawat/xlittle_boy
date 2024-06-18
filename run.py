import sys
sys.path.insert(0, "main/templates")
from _utils import Utils

if __name__ == "__main__": 
    stock_name = "COIN"
    start_test_date = "2024-04-15"
    n_train_periods = 2 # Unit: Day
    n_test_periods = 1 # Unit: Day
    multiplier = 15 # Number of second/minute/hour/day
    timespan = "minute" # Unit of multiplier
    # list_n_ema = [[12, 24], [6, 12]]
    # list_model_names = ["lstm_model_v_1_0", "attention_model_v_1_0"]
    ListPredictionTypes = ["low", "high"]
    # ListPredictionTypes = ["low"]
    # list_n_prediction_periods = [0, 1] # Minimum: 0
    # list_n_lags = [10, 20]
    # ListIsCrossValidations = [True, False]
    # list_n_validation_siz1 = [0.2, 0.3]
    # list_n_epochs = [1, 2]
    # list_n_batch_sizes = [100, 200]
    # threshold_between_actual_and_predicted_values = 0.3

    list_n_atr = [14, 28]
    list_n_ema = [6, 12, 24]
    list_n_macd = [[12, 26, 9]]
    list_n_rsi = [14, 28]
    list_n_tr = [1, 14]
    """
        ["lstm_model_v_1_0", "lstm_model_v_1_1", lstm_model_v_2_1, "attention_model_v_1_0"]
    """
    list_model_names = ["lstm_model_v_1_0"]
    list_n_prediction_periods = [1] # Minimum: 0
    list_n_lags = [30]
    ListIsNormalization = [True]
    ListIsCrossValidations = [True]
    list_n_validation_sizes = [0.2]
    list_n_epochs = [1]
    list_n_batch_sizes = [1000]
    threshold_between_actual_and_predicted_values = 0.5
    win_rate_treshold = 0 # Unit: Percentage

    IsSaveData = True
    IsSaveModel = False
    IsSaveScaler = False

    # print(f"ListIsCrossValidations: \n{ListIsCrossValidations}")

    Utils(
        stock_name,
        start_test_date,
        n_train_periods,
        n_test_periods,
        multiplier,
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
    ).run()

    