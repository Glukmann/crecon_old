# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import plotly.offline as opy
import plotly.graph_objs as go
from .fbprophet_local import Graph_prophet
from .keras_local import Graph_keras
from .arima_local import Graph_arima

class Metods:

    fbprophet = False
    keras = False
    arima = False

class Graph():
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

    def universal_prognoz(self, data_df, Metods):
        figure_or_data = []

        if Metods.fbprophet:
            gprophets= Graph_prophet()
            x_prophets, y_prophets = gprophets.prognoz(data_df)
            figure_or_data.append(go.Scatter(x=x_prophets, y=y_prophets, name="FbProphet", line=dict(dash="dot")))

        if Metods.keras:
            gkeras = Graph_keras()
            x_keras, y_keras = gkeras.prognoz(data_df)
            figure_or_data.append(go.Scatter(x=x_keras, y=y_keras, name="Keras", line=dict(dash="dot")))

        if Metods.arima:
            garima = Graph_arima()
            x_arima, y_arima = garima.prognoz(data_df)
            figure_or_data.append(go.Scatter(x=x_arima, y=y_arima, name="ARIMA", line=dict(dash="dot")))

        vertical = [row.sumsale for row in data_df]
        horizontal = [row.sale_date for row in data_df]
        figure_or_data.append(go.Scatter(x=horizontal, y=vertical, name="current data", mode="lines+markers"))

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

        plot_html = opy.plot(fig, True, "open in new window", True, "div")

        return plot_html
