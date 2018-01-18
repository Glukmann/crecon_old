# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic.base import TemplateView
from fbprophet import Prophet
import pandas as pd

import numpy as np
# pip install fbprophet


class Graph(TemplateView):
    def get_context_data(self, data_df):
        vertical = [row.sumsale for row in data_df]
        horizontal = [row.sale_date for row in data_df]

        figure_or_data = [go.Scatter(x=horizontal, y=vertical, name="current data", mode="lines+markers")]

        layout = dict(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label='1 month',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6 month',
                             step='month',
                             stepmode='backward'),
                        dict(count=1,
                             label='1 month',
                             step='year',
                             stepmode='backward'),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(),
                type='date'
            )
        )

        fig = dict(data = figure_or_data, layout=layout)

        plot_html = opy.plot(
            fig, True, 'open in new window', True, "div")

        return plot_html

    def prognoz(self, data_df):
        predictions = 60

        vertical = [row.sumsale for row in data_df]
        horizontal = [row.sale_date for row in data_df]

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

        # m = Prophet(weekly_seasonality=False)
        # m.add_seasonality(name='monthly', period=30.5, fourier_order=5)
        m.fit(df)

        future = m.make_future_dataframe(periods=predictions)
        future['nfl_sunday'] = future['ds'].apply(nfl_sunday)

        future['cap'] = 4000
        future['floor'] = 1500

        forecast = m.predict(future)

        #plot_html = m.plot(forecast)

        #plot_html = m.plot_components(forecast)

        figure_or_data = [go.Scatter(x=horizontal, y=vertical, name="current data", mode="lines+markers"),
                          go.Scatter(x=forecast.ds, y=forecast.yhat, name="prophet",
                                     line=dict(dash="dot"))]

        layout = dict(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label='1 month',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6 month',
                             step='month',
                             stepmode='backward'),
                        dict(count=1,
                             label='1 year',
                             step='year',
                             stepmode='backward'),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(),
                type='date'
            )
        )

        fig = dict(data=figure_or_data, layout=layout)

        plot_html = opy.plot(
            fig, True, "open in new window", True, "div")

        return plot_html