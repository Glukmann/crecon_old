# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fbprophet import Prophet
import pandas as pd

# pip install fbprophet

class Graph_prophet():
    @staticmethod
    def prognoz(data_df):
        predictions = 60

        y = [row.sumsale for row in data_df]
        ds = [row.sale_date for row in data_df]

        for index in range(len(ds)):
            ds[index] = ds[index].strftime('%Y-%m-%d')

        df = pd.DataFrame({'y' : y,
                           'ds' : ds})

        # df['y'] = np.log(df['y'])

        ngod = pd.DataFrame({
            'holiday': 'ngod',
            'ds': pd.to_datetime(['2015-12-30', '2015-12-30', '2016-12-30', '2017-12-30']),
            'lower_window': -10,
            'upper_window': 0,
        })
        valday = pd.DataFrame({
            'holiday': 'valday',
            'ds': pd.to_datetime(['2015-02-14', '2016-02-14', '2017-02-14', '2018-02-14',
                                  '2015-03-08', '2016-03-08', '2017-03-08', '2018-02-14']),
            'lower_window': -3,
            'upper_window': 1,
        })
        holidays = pd.concat((ngod, valday))

        def nfl_sunday(ds):
            date = pd.to_datetime(ds)
            if date.weekday() == 6:
                return 1
            else:
                return 0

        df['nfl_sunday'] = df['ds'].apply(nfl_sunday)

        df['cap'] = 4000
        df['floor'] = 1500

        m = Prophet(holidays=holidays, holidays_prior_scale=10, changepoint_prior_scale=0.05, growth='logistic', mcmc_samples=10, yearly_seasonality=True)
        m.add_regressor('nfl_sunday')
        m.add_seasonality(
            name='weekly', period=7, fourier_order=3, prior_scale=0.1)

        m.fit(df)

        future = m.make_future_dataframe(periods=predictions)
        future['nfl_sunday'] = future['ds'].apply(nfl_sunday)

        future['cap'] = 4000
        future['floor'] = 1500

        forecast = m.predict(future)

        x = forecast.ds
        y = forecast.yhat
        return x,y