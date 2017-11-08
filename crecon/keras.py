# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from keras.models import Sequential
from keras.callbacks import ReduceLROnPlateau
from keras import optimizers
from keras.layers import Dense, Activation, LeakyReLU, BatchNormalization
import plotly.offline as opy
import plotly.graph_objs as go
import numpy as np

# pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

class Graph_keras(TemplateView):
    def prognoz(self, data_df):
        vertical = [row.sumsale for row in data_df]
        horizontal = [row.sale_date for row in data_df]
        forecast=[]

        model = Sequential()
        model.add(Dense(64, input_dim=30))
        model.add(BatchNormalization())
        model.add(LeakyReLU())
        model.add(Dense(2))
        model.add(Activation('softmax'))

        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.9, patience=5, min_lr=0.001, verbose=1)
        model.compile(loss='categorical_crossentropy',
                      metrics=['accuracy'])

        history = model.fit(vertical, horizontal,
                            nb_epoch=50,
                            batch_size=128,
                            verbose=1,
                            validation_data=(horizontal, vertical),
                            shuffle=True,
                            callbacks=[reduce_lr])

        pred = model.predict(np.array(horizontal))
        original = vertical
        predicted = pred

        figure_or_data = [go.Scatter(x=horizontal, y=vertical, name="current data", mode="lines+markers"),
                          go.Scatter(x=forecast.ds, y=forecast.yhat, name="Keras",
                                     line=dict(dash="dot"))]

        plot_html = opy.plot(
            figure_or_data, True, "Open in new window", True, "div")
        return plot_html