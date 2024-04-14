from _libs import *

def indicator_macd(self):
    for _list_n_macd in self.list_n_macd:
        ### Calc macd
        fast_ema_values = ta.ema(self.cleaned_data.close, _list_n_macd[0])
        slow_ema_values = ta.ema(self.cleaned_data.close, _list_n_macd[1])
        macd_values = fast_ema_values - slow_ema_values

        ### Calc signal line
        signal_values = ta.ema(macd_values, _list_n_macd[2])

        ### Update cleaned data
        self.cleaned_data[f"macd_{_list_n_macd[0]}_{_list_n_macd[1]}_{_list_n_macd[2]}"] = macd_values
        self.cleaned_data[f"signal_line_{_list_n_macd[0]}_{_list_n_macd[1]}_{_list_n_macd[2]}"] = signal_values