from _libs import *

def get_data(self):
    client = RESTClient(api_key="7PZTsP8NHCZy0cEsWRlgFaSa2Q8zm8Zb")

    ### List Aggregates (Bars)
    aggs = []
    for a in client.list_aggs(ticker=self.stock_name, multiplier=self.n_multiplier, timespan=self.timespan, from_=self.start_train_date, to=self.end_test_date+relativedelta(days=self.n_test_periods), limit=50000): # -relativedelta(days=1): For generating indicators without missing values
        aggs.append(a)

    self.data = pd.DataFrame(aggs)