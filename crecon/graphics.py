# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic.base import TemplateView
from .fbprophet_local import Graph_prophet
from .keras_local import Graph_keras

class metods:
    fbprophet= False
    keras=False

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

    def universal_prognoz(self, data_df, metods):
        figure_or_data = []

        if metods.fbprophet:
            x_prophets, y_prophets = Graph_prophet.prognoz(self,data_df)
            figure_or_data.append(go.Scatter(x=x_prophets, y=y_prophets, name="FbProphet", line=dict(dash="dot")))


        if metods.keras:
            x_keras, y_keras = Graph_keras.prognoz(self,data_df)
            figure_or_data.append(go.Scatter(x=x_keras, y=y_keras, name="Keras", line=dict(dash="dot")))

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
