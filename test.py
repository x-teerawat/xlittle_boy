from sklearn.preprocessing import MinMaxScaler
import numpy as np

x = np.arange(11).reshape(-1, 1)
y = np.arange(11, 21).reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0,1))
old_scaler = scaler.fit_transform(x)

print(f"x: {x}")
print(f"y: {y}")
print(f"scaler: {scaler}")
print(f"old_scaler: {old_scaler}")
print(f"new_scaler: {scaler.fit(y)}")
print(f"transfrom x: {scaler.transform(x)}")
print(f"transfrom y: {scaler.transform(y)}")
# print(f"new_scaler: {scaler.transform(y)}")