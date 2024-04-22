from _libs import *

def clean_data(self, prepared_data):
    unique_date = prepared_data.date.unique()
    lst_cleaned_data = []

    if self.timespan != 'day':
        for _date in unique_date:
            prepared_data_copy = prepared_data[prepared_data.date==_date].copy()
            if self.timespan == 'second':
                selected_end_time = (pd.Timestamp('20:00:00')-relativedelta(seconds=self.n_multiplier)).strftime('%H:%M:%S')
            elif self.timespan == 'minute':
                selected_end_time = (pd.Timestamp('20:00:00')-relativedelta(minutes=self.n_multiplier)).strftime('%H:%M:%S')
            elif self.timespan == 'hour':
                selected_end_time = (pd.Timestamp('20:00:00')-relativedelta(hours=self.n_multiplier)).strftime('%H:%M:%S')

            ### Determine start and end trading time
            if prepared_data_copy.time[0] != "04:00:00": # Start trading time
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + " 04:00:00").tz_localize('US/Eastern')] = np.nan
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + " 04:00:00").tz_localize('US/Eastern'), 'date'] = prepared_data_copy.date[0]
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + " 04:00:00").tz_localize('US/Eastern'), 'time'] = prepared_data_copy.time[0]
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + " 04:00:00").tz_localize('US/Eastern'), 'day'] = prepared_data_copy.day[0]
            if prepared_data_copy.time[-1] != selected_end_time: # End trading time
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + f" {selected_end_time}").tz_localize('US/Eastern')] = np.nan
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + f" {selected_end_time}").tz_localize('US/Eastern'), 'date'] = prepared_data_copy.date[0]
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + f" {selected_end_time}").tz_localize('US/Eastern'), 'time'] = prepared_data_copy.time[0]
                prepared_data_copy.loc[pd.Timestamp(prepared_data_copy.date[0] + f" {selected_end_time}").tz_localize('US/Eastern'), 'day'] = prepared_data_copy.day[0]
            prepared_data_copy.sort_index(inplace=True)

            ### Search missing time
            prepared_data_copy['diff_times'] = prepared_data_copy.index.to_series().diff()
            if self.timespan == 'second':
                prepared_data_copy['diff_times'] = [prepared_data_copy.diff_times[i].seconds for i in range(len(prepared_data_copy))]
            elif self.timespan == 'minute':
                prepared_data_copy['diff_times'] = [prepared_data_copy.diff_times[i].seconds/60 for i in range(len(prepared_data_copy))]
            elif self.timespan == 'hour':
                prepared_data_copy['diff_times'] = [prepared_data_copy.diff_times[i].seconds/60/60 for i in range(len(prepared_data_copy))]
            prepared_data_copy['n_missing_times'] = prepared_data_copy.diff_times-self.n_multiplier
            prepared_data_copy.n_missing_times.fillna(0, inplace=True)
            
            ### Generate missing times
            if self.timespan == 'second':
                lst_missing_time = [[prepared_data_copy.index[i-1]+relativedelta(seconds=n_missing_times) for n_missing_times in range(1, int(prepared_data_copy.n_missing_times[i])+1)] for i in range(len(prepared_data_copy)) if prepared_data_copy.n_missing_times[i] != 0]
            elif self.timespan == 'minute':
                lst_missing_time = [[prepared_data_copy.index[i-1]+relativedelta(minutes=n_missing_times) for n_missing_times in range(1, int(prepared_data_copy.n_missing_times[i])+1)] for i in range(len(prepared_data_copy)) if prepared_data_copy.n_missing_times[i] != 0]
            elif self.timespan == 'hour':
                lst_missing_time = [[prepared_data_copy.index[i-1]+relativedelta(hours=n_missing_times) for n_missing_times in range(1, int(prepared_data_copy.n_missing_times[i])+1)] for i in range(len(prepared_data_copy)) if prepared_data_copy.n_missing_times[i] != 0]
            lst_missing_time = [
                missing_time
                for lst_in_lst_missing_time in lst_missing_time
                for missing_time in lst_in_lst_missing_time
            ] # Flat list in list
            # print(f"lst_missing_time: {lst_missing_time}") 
            prepared_data_missing_time = pd.DataFrame(index=lst_missing_time) # Convert list to dataframe

            ### Concat missing time with existing data
            prepared_data_copy = pd.concat([prepared_data_copy, prepared_data_missing_time], axis=0)
            prepared_data_copy.sort_index(inplace=True)

            ### Check
            n_missing_values = prepared_data_copy[(prepared_data_copy.index>=f"{_date} 04:00:00")*(prepared_data_copy.index<=f"{_date} {selected_end_time}")].open.isna().sum()
            n_data = len(prepared_data_copy[(prepared_data_copy.index>=f"{_date} 04:00:00")*(prepared_data_copy.index<=f"{_date} {selected_end_time}")])
            print(f"In {_date} from 04:00:00 to {selected_end_time}, There're missing values: {n_missing_values}/{n_data} ({np.round(n_missing_values/n_data*100, 4)}%)")

            ### Fill missing values (Assumption: The price has not changed, if there's no volumn)
            prepared_data_copy.volume.fillna(0, inplace=True)
            prepared_data_copy.fillna(method='ffill', inplace=True)
            
            ### Select preferred columns
            prepared_data_copy = prepared_data_copy[['open', 'high', 'low', 'close', 'volume']]

            ### Append
            lst_cleaned_data.append(prepared_data_copy)

            ### Fill missing values with previous 14 days
            # prepared_data_copy['open'] = prepared_data_copy.open.fillna(prepared_data_copy.open.rolling(window=14, min_periods=1).mean())
            # prepared_data_copy['high'] = prepared_data_copy.high.fillna(prepared_data_copy.high.rolling(window=14, min_periods=1).mean())
            # prepared_data_copy['low'] = prepared_data_copy.low.fillna(prepared_data_copy.low.rolling(window=14, min_periods=1).mean())
            # prepared_data_copy['close'] = prepared_data_copy.close.fillna(prepared_data_copy.close.rolling(window=14, min_periods=1).mean())
            # ### Incase, There are many continue missing values 
            # missing_idx = prepared_data_copy[prepared_data_copy.open.isna()].index
            # for missing_date in missing_idx:
            #     print(prepared_data_copy.loc[:missing_date, 'open'].iloc[-15:-1])
            #     mean_open = prepared_data_copy.loc[:missing_date, 'open'].iloc[-15:-1].mean()
            #     mean_high = prepared_data_copy.loc[:missing_date, 'high'].iloc[-15:-1].mean()
            #     mean_low = prepared_data_copy.loc[:missing_date, 'low'].iloc[-15:-1].mean()
            #     mean_close = prepared_data_copy.loc[:missing_date, 'close'].iloc[-15:-1].mean()

            #     prepared_data_copy.loc[missing_date, 'open'] = mean_open
            #     prepared_data_copy.loc[missing_date, 'high'] = mean_high
            #     prepared_data_copy.loc[missing_date, 'low'] = mean_low
            #     prepared_data_copy.loc[missing_date, 'close'] = mean_close

            # ### Determine open market
            # prepared_data_copy = prepared_data_copy[(prepared_data_copy.index>=f"{_date} 04:00:00")*(prepared_data_copy.index<=f"{_date} 19:59:59")]

            # ### Select preferred columns
            # prepared_data_copy = prepared_data_copy[['open', 'high', 'low', 'close']]
            # print(tabulate(prepared_data_copy, prepared_data_copy.columns))
            
            # ### Append
            # lst_cleaned_data.append(prepared_data_copy)

        ### Concat
        cleaned_data = pd.concat(lst_cleaned_data)
    
    else:
        cleaned_data = prepared_data.copy()

    return cleaned_data