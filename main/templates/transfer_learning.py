from load_model_weights import load_model_weights

import sys
sys.path.insert(0, "../templates")
from _libs import *

def transfer_learning(self):
    # load_model_weights(self) 
    # print("asdf")
    # print(f"self.model_weights: \n{self.model_weights}")
    # print(f"{self.file_name}.h5")
    ### Build model
    base_model = Sequential()
    base_model.add(Input(shape=(self.x_train.shape[1], self.x_train.shape[2])))
    # base_model.add(Input(shape=(1, 1)))
    base_model.add(Xception(weights=f"{self.file_name}.h5", include_top=False))
    base_model.add(LSTM(10))
    base_model.add(Dropout(0.2))
    base_model.add(Dense(1))
    base_model.summary()
    base_model.compile(optimizer='adam', loss='mse')
    base_model.trainable = False

