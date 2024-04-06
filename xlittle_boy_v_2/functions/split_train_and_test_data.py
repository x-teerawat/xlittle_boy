def split_train_and_test_data(self):
    self.train_data = self.prepared_data[self.prepared_data.index<self.start_test_date]
    self.test_data = self.prepared_data[self.prepared_data.index>=self.start_test_date]