from _libs import *

def split_train_and_test_data(self):
    self.train_data = self.prepared_data[self.prepared_data.index<self.start_test_date]

    part_of_train_data = self.train_data.tail(self.n_lags-1) # -1: Because there's first value of test data
    self.test_data = self.prepared_data[self.prepared_data.index>=self.start_test_date]
    self.test_data = pd.concat([part_of_train_data, self.test_data])

    # print(tabulate(self.train_data, self.train_data.columns))
    # print(tabulate(self.test_data, self.test_data.columns))