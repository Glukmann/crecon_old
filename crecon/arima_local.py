# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pyflux as pf
from datetime import datetime, timedelta


class Graph_arima():
    def prognoz(self, data_df):
        y = [row.sumsale for row in data_df]
        ds = [row.sale_date for row in data_df]



        df = pd.DataFrame({'y': y,
                           'ds': ds})

        model = pf.ARIMA(data=df, ar=4, ma=4, integ=0, target='y')
        x = model.fit()

        y=x.data

        # model.plot_fit(figsize=(15, 5))

        predict = model.predict_is(h=60, fit_once=True, fit_method='MLE')

        # for index in range(len(ds)):
        #     ds[index] = ds[index].strftime('%Y-%m-%d')
        i=1
        while i<= 64:
            ds.append(ds[-1]+timedelta(days=1))
            i=i+1

        ds = pd.Series(ds)
        y= y.tolist()
        i = 1
        while i<= 4:
            y.insert(0, 0)
            i=i+1

        for row in predict.itertuples():
            y.append(row.Series)

        return ds, y