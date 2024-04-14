from _libs import *

def indicator_tr(self):
    for i in self.list_n_tr:
        tr_values = np.maximum.reduce([
            abs(self.cleaned_data.high - self.cleaned_data.low),
            abs(self.cleaned_data.high - self.cleaned_data.close.shift(i)),
            abs(self.cleaned_data.low - self.cleaned_data.close.shift(i))
        ])
        
        ### Update
        self.cleaned_data[f"tr_{i}"] = tr_values