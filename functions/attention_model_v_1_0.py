import sys
sys.path.insert(0, "../templates")
from _libs import *

def attention_model_v_1_0(self):
    self.model = Sequential()
    self.model.add(Input(shape=(self.x_train.shape[1], self.x_train.shape[2])))
    self.model.add(GRU(64, return_sequences=True))
    self.model.add(LSTM(32, return_sequences=True))
    self.model.add(Attention(32))
    self.model.add(Dense(32, activation="relu"))
    self.model.add(Dropout(0.2))
    self.model.add(Dense(1))
    # self.model.summary()
    self.model.compile(optimizer='adam', loss='mse')
    history = self.model.fit(self.x_train, self.y_train, epochs=self.n_epochs, batch_size=self.n_batch_size, verbose=0)