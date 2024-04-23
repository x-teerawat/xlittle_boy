import pickle

def save_dict_to_pickle(self):
    with open(f'list_scalers__{self.params}.pkl', 'wb') as f:
        pickle.dump(self.list_scalers, f)