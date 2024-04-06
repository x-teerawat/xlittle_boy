from lstm_model_v_1_0 import lstm_model_v_1_0
from lstm_model_v_2_0 import lstm_model_v_2_0
from lstm_model_v_2_1 import lstm_model_v_2_1
from lstm_model_v_2_2 import lstm_model_v_2_2
from lstm_model_v_2_3 import lstm_model_v_2_3
from lstm_model_v_2_4 import lstm_model_v_2_4
from lstm_model_v_2_5 import lstm_model_v_2_5
from lstm_model_v_2_6 import lstm_model_v_2_6
from lstm_model_v_2_7 import lstm_model_v_2_7
from lstm_model_v_2_8 import lstm_model_v_2_8
from lstm_model_v_2_9 import lstm_model_v_2_9
from lstm_model_v_2_10 import lstm_model_v_2_10

from attention_model_v_1_0 import attention_model_v_1_0

def _build_models(self):
    if self.model_name == "lstm_model_v_1_0":
        lstm_model_v_1_0(self)

    if self.model_name == "lstm_model_v_2_0":
        lstm_model_v_2_0(self)

    if self.model_name == "lstm_model_v_2_1":
        lstm_model_v_2_1(self)

    if self.model_name == "lstm_model_v_2_2":
        lstm_model_v_2_2(self)

    if self.model_name == "lstm_model_v_2_3":
        lstm_model_v_2_3(self)

    if self.model_name == "lstm_model_v_2_4":
        lstm_model_v_2_4(self)
    
    if self.model_name == "lstm_model_v_2_5":
        lstm_model_v_2_5(self)

    if self.model_name == "lstm_model_v_2_6":
        lstm_model_v_2_6(self)

    if self.model_name == "lstm_model_v_2_7":
        lstm_model_v_2_7(self)

    if self.model_name == "lstm_model_v_2_8":
        lstm_model_v_2_8(self)

    if self.model_name == "lstm_model_v_2_9":
        lstm_model_v_2_9(self)
    
    if self.model_name == "lstm_model_v_2_10":
        lstm_model_v_2_10(self)

    if self.model_name == "attention_model_v_1_0":
        attention_model_v_1_0(self)  