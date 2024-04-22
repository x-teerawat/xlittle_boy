import sys
sys.path.insert(0, "../templates")
from _libs import *

def evaluate_model(self, y_actual):
    ### Result (actual_value, predicted_value, pct_change_between_actual_and_prediction, win_loss)
    if self.IsNormalization:
        y_actual = self.list_scalers[self.prediction_column_nth].inverse_transform(y_actual)

    result_data = pd.DataFrame({
        "actual_value": y_actual.flatten(),
        "predicted_value": self.predicted_values.flatten()
    }, index=self.selected_train_data.index[-y_actual.shape[0]:])
    result_data["pct_change_between_actual_and_prediction"] = abs((result_data.actual_value-result_data.predicted_value)/result_data.predicted_value*100)
    result_data["win_loss"] = [1 if i<=self.threshold_between_actual_and_predicted_values else 0 for i in result_data.pct_change_between_actual_and_prediction]
    print(tabulate(result_data, result_data.columns))

    ### Win rate
    try:
        # print(f"result_data.win_loss.value_counts()[1]: \n{result_data.win_loss.value_counts()[1]}")
        self.win_rate = result_data.win_loss.value_counts()[1]/len(result_data)*100
    except: ### Incase, loss 100%
        self.win_rate = 0
        pass
    print(f"win_rate (%): {self.win_rate}")