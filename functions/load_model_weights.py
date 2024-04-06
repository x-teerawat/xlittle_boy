import pickle

def load_model_weights(self):
    with open(f"{self.file_name}.pkl", "rb") as f:
        self.model_weights = pickle.load(f)