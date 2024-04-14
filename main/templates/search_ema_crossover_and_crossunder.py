from _libs import *

def search_ema_crossover_and_crossunder(self):
    ema_cols = self.cleaned_data.columns.str.contains('ema')
    print(f"ema_cols: {ema_cols}")
    ema_data = self.cleaned_data.loc[:, ema_cols].copy()
    print(tabulate(ema_data, ema_data.columns))