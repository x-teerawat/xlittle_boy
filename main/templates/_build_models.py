import sys
sys.path.insert(0, "main/models")
from _all_models import *

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