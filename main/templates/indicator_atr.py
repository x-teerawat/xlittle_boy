from _libs import *

def indicator_atr(self):
    for i in self.list_n_atr:
        atr_values = ta.atr(self.cleaned_data.high, self.cleaned_data.low, self.cleaned_data.close, i)

        ### Update
        self.cleaned_data[f"atr_{i}"] = atr_values