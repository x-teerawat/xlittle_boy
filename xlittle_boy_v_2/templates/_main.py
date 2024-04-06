from _utils import *

if __name__ == "__main__": 
    stock_name = "COIN"
    start_test_date = "2024-03-27"
    n_train_periods = 1000 # Unit: Day
    n_test_periods = 1 # Unit: Day
    multiplier = 60 # Number of second/minute/hour/day
    timespan = "minute" # Unit of multiplier
    # list_n_ema = [[12, 24], [6, 12]]
    # list_model_names = ["lstm_model_v_1_0", "attention_model_v_1_0"]
    # ListPredictionType = ["low", "high"]
    # list_n_prediction_periods = [0, 1] # Minimum: 0
    # list_n_lags = [10, 20]
    # ListIsCrossValidation = [True, False]
    # list_n_validation_siz1 = [0.2, 0.3]
    # list_n_epochs = [1, 2]
    # list_n_batch_sizes = [100, 200]
    # threshold_between_actual_and_predicted_values = 0.3

    list_n_ema = [6, 12, 24]
    """
        ["lstm_model_v_1_0", "lstm_model_v_1_1", lstm_model_v_2_1, "attention_model_v_1_0"]
    """
    list_model_names = ["lstm_model_v_2_10"]
    ListPredictionType = ["low", "high"]
    list_n_prediction_periods = [1] # Minimum: 0
    list_n_lags = [16]
    ListIsNormalization = [True]
    ListIsCrossValidation = [False]
    list_n_validation_sizes = [0.2]
    list_n_epochs = [10]
    list_n_batch_sizes = [100]
    threshold_between_actual_and_predicted_values = 0.3
    win_rate_treshold = 70 # Unit: Percentage

    IsSaveData = False
    IsSaveModel = False

    # print(f"ListIsCrossValidation: \n{ListIsCrossValidation}")

    Utils(
        stock_name,
        start_test_date,
        n_train_periods,
        n_test_periods,
        multiplier,
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
    ).run()
