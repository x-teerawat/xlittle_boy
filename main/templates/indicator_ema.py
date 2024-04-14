import pandas_ta as ta

def indicator_ema(self):
    for n_ema in self.list_n_ema:
        # print(f"n_ema: \n{n_ema}")
        ema_values = ta.ema(self.cleaned_data.close, n_ema)

        self.cleaned_data[f'ema_{n_ema}'] = ema_values