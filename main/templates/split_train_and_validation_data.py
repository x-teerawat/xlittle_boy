# import sys
# sys.path.insert(0, "../templates")
# from _libs import *

def split_train_and_validation_data(self):
    ### Split validation data
    train_size = int(self.x.shape[0]*(1-self.n_validation_size))
    self.x_train = self.x[:train_size, :, :]
    self.y_train = self.y[:train_size]
    self.x_valid = self.x[train_size:, :, :]
    self.y_valid = self.y[train_size:]

    # print(f"self.x_train: {self.x_train}")
    # print(f"self.y_train: {self.y_train}")
    # print(f"self.x_valid: {self.x_valid}")
    # print(f"self.x_valid: {self.x_valid}")
    # print(f"self.y_valid: {self.y_valid}")
    # print(f"self.y_valid.shape: {self.y_valid.shape}")

    if self.IsNormalization:
        self.y_valid = self.list_scalers[self.prediction_column_nth].inverse_transform(self.y_valid)

    print(f"self.x_train.shape: {self.x_train.shape}")
    print(f"self.y_train.shape: {self.y_train.shape}")
    print(f"self.x_valid.shape: {self.x_valid.shape}")
    print(f"self.x_valid.shape: {self.x_valid.shape}")
    print(f"self.y_valid.shape: {self.y_valid.shape}")