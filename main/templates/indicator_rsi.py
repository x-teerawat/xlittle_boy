from _libs import *

def indicator_rsi(self):
    for i in self.list_n_rsi:
        rsi_values = ta.rsi(self.cleaned_data.close, i)

        ### Update
        self.cleaned_data[f"rsi_{i}"] = rsi_values