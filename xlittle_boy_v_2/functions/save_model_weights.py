# import pickle
import h5py
import numpy as np

def save_model_weights(self):
    # with open(f"{self.file_name}.pkl", "wb") as f:
    #     pickle.dump(self.model_weights, f)

    with h5py.File(f'{self.file_name}.h5','w') as h5f:
        h5f.create_dataset("model_weights", data=np.asarray(self.model_weights) )

    # f = h5py.File(f'{self.file_name}.h5', 'r')
    # print(f"f: \n{f}")