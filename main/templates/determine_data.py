from _libs import *

def determine_data(self):
    self.cleaned_data = self.cleaned_data[self.cleaned_data.index>=self.start_train_date.tz_localize("US/Eastern")]
    