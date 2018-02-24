# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.callbacks import ReduceLROnPlateau
from keras.layers import Dense, Activation, LeakyReLU, BatchNormalization
import numpy as np
import pandas as pd
from keras.losses import logcosh

# pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

class Graph_keras():
    def prognoz(self, data_df):
        horizontal = [row.sale_date for row in data_df]

        horizontal_date = [row.sale_date for row in data_df]

        for index in range(len(horizontal)):
            horizontal[index] = horizontal[index].strftime('%Y-%m-%d')

        q = data_df.values('sale_date')
        df_date = pd.DataFrame.from_records(q)

        vertical_x = [row.sumsale for row in data_df]

        for index in range(len(vertical_x)):
            a= [vertical_x[index]]
            vertical_x[index]=a

        y_train_y = vertical_x

        y_train = np.array(vertical_x)

        df_date['year'] = pd.Series(1, index=df_date.index)
        df_date['month'] = pd.Series(1, index=df_date.index)
        df_date['day'] = pd.Series(1, index=df_date.index)
        df_date['week'] = pd.Series(1, index=df_date.index)

        x_train = df_date.as_matrix()

        for index in x_train:
            index[1] = index[0].strftime('%Y-%m-%d')[0:4]

        for index in x_train:
            index[2] = index[0].strftime('%Y-%m-%d')[5:7]

        for index in x_train:
            index[3] = index[0].strftime('%Y-%m-%d')[8:10]

        for index in x_train:
            index[4] = index[0].weekday()

        x_train = np.delete(x_train, 0,1)

        x_train = x_train.astype('float32')
        y_train = y_train.astype('float32')

        mean = x_train.mean(axis=0)
        std = x_train.std(axis=0)
        x_train -= mean
        x_train /= std

        model = Sequential()
        model.add(Dense(400, input_dim=4, activation="relu", kernel_initializer="normal"))
        model.add(Dense(300, activation="relu", kernel_initializer="normal"))
        model.add(Dense(200, activation="relu", kernel_initializer="normal"))
        model.add(Dense(100, activation="relu", kernel_initializer="normal"))
        model.add(Dense(50, activation="relu", kernel_initializer="normal"))
        model.add(Dense(1, activation="relu", kernel_initializer="normal"))
        model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
        model.fit(x_train, y_train_y, epochs=100, validation_split=0.1, verbose=2)

        # mse, mae = model.evaluate(x_train, y_train, verbose=0)

        pred = model.predict(x_train)
        plan_list = []
        res_list = []
        for i in range(len(x_train)):
            # print("Date: {}, plan: {}, fact {}".format(x_train[i], pred[i][0], y_train[i][0]))
            plan_list.append(pred[i][0])
            res_list.append(y_train[i][0])

        x = horizontal_date
        y = plan_list

        return x,y