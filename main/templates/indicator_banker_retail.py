from _libs import *

def indicator_banker_retail(self):
    ### Default banker and retail values
    RSIPeriodBanker     = 50
    SensitivityBanker   = 1.5
    RSIBaseBanker       = 50
    
    RSIPeriodHotMoney   = 40
    RSIBaseHotMoney     = 30
    SensitivityHotMoney = 0.7

    ### Compute banker and retail values
    rsi_values = ta.rsi(self.cleaned_data.close, RSIPeriodBanker)
    banker_values = SensitivityBanker * (rsi_values-RSIBaseBanker)
    banker_values[banker_values > 20] = 20
    banker_values[banker_values < 0] = 0
    banker_values = banker_values / 20 *100

    rsi_values = ta.rsi(self.cleaned_data.close, RSIPeriodHotMoney)
    retail_values = SensitivityHotMoney * (rsi_values-RSIBaseHotMoney)
    retail_values[retail_values > 20] = 20
    retail_values[retail_values < 0] = 0
    retail_values = 100 - (retail_values/20*100)

    ### Update
    self.cleaned_data["banker"] = banker_values
    self.cleaned_data["retail"] = retail_values