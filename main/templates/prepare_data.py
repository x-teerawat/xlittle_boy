from _libs import *

def prepare_data(self):
    ### Prep data
    self.prepared_data = self.data.copy()
    self.prepared_data['timestamp'] = pd.to_datetime(self.prepared_data.timestamp, unit="ms") # Convert timestamp
    ### Convert time zone
    est = pytz.timezone('US/Eastern')
    utc = pytz.utc
    self.prepared_data['timestamp'] = [self.prepared_data['timestamp'][i].replace(tzinfo=utc).astimezone(est) for i in range(len(self.prepared_data))]
    # self.prepared_data['timestamp'] = [self.prepared_data['timestamp'][i].replace(tzinfo=None) for i in range(len(self.prepared_data))] # Remove timezone
    self.prepared_data['date'] = [self.prepared_data.timestamp[i].strftime("%Y-%m-%d") for i in range(len(self.prepared_data))] # Date
    self.prepared_data['time'] = [self.prepared_data.timestamp[i].strftime("%H:%M:%S") for i in range(len(self.prepared_data))] # Time
    self.prepared_data['day'] = [self.prepared_data.timestamp[i].strftime("%a") for i in range(len(self.prepared_data))] # Day
    self.prepared_data.index = self.prepared_data.timestamp # Set index
    self.prepared_data.index.name = None # Remove index name
    self.prepared_data.drop(columns=['vwap', 'timestamp', 'transactions', 'otc'], inplace=True) # Drop timestamp column
