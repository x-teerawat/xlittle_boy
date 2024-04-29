# from sklearn.preprocessing import MinMaxScaler
# import numpy as np

# x = np.arange(11).reshape(-1, 1)
# y = np.arange(11, 21).reshape(-1, 1)
# scaler = MinMaxScaler(feature_range=(0,1))
# old_scaler = scaler.fit_transform(x)

# print(f"x: {x}")
# print(f"y: {y}")
# print(f"scaler: {scaler}")
# print(f"old_scaler: {old_scaler}")
# print(f"new_scaler: {scaler.fit(y)}")
# print(f"transfrom x: {scaler.transform(x)}")
# print(f"transfrom y: {scaler.transform(y)}")
# # print(f"new_scaler: {scaler.transform(y)}")

import requests

def send_line_notification(message, token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print('Notification sent successfully.')
    else:
        print('Failed to send notification.')

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token obtained from Line Notify
access_token = 'xG7JEXN80ITRI24my083Q3UieVXR3XxlKsrEJrFLV7W'

# Replace 'Your notification message' with the message you want to send
notification_message = 'Your notification message'

# Send the notification
send_line_notification(notification_message, access_token)
