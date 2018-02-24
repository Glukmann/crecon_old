from pandas import read_csv,DataFrame
import keras
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense


df =  read_csv('C:\\base\\444.csv',';')

x_train_date = df.as_matrix(['day','mounth','year'])
y_train = df.as_matrix(['value'])

x_train = x_train_date.astype('float32')
y_train = y_train.astype('float32')

mean = x_train.mean(axis=0)
std = x_train.std(axis=0)
x_train -= mean
x_train /= std

model = Sequential()
model.add(Dense(400, input_dim=3, activation="relu", kernel_initializer="normal"))
model.add(Dense(300, activation="relu", kernel_initializer="normal"))
model.add(Dense(200, activation="relu", kernel_initializer="normal"))
model.add(Dense(100, activation="relu", kernel_initializer="normal"))
model.add(Dense(50, activation="relu", kernel_initializer="normal"))
model.add(Dense(1, activation="relu", kernel_initializer="normal"))
# model = Sequential()
# model.add(LSTM(60, batch_input_shape=(batch_size, tsteps, 1)))

model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
model.fit(x_train, y_train, epochs=100, validation_split=0.1, verbose=2)

mse, mae = model.evaluate(x_train, y_train, verbose=0)

print("mae:", mae)  

#date = datetime(2018, 1, 1)
#day = timedelta(days=1)

#x_test_dates = []
#for i in range(365):
    #x_test_dates.append([date.day,date.month,date.year])
    #date += day

#x_test_dates = numpy.array(x_test_dates)        
#x_test = x_test_dates.astype(float)
#x_test -= mean
#x_test /= std

pred = model.predict(x_train)
plan_list = []
res_list = []
for i in range(len(x_train)):
    # print("Date: {}, plan: {}, fact {}".format(x_train_date[i],pred[i][0],y_train[i][0]))
    plan_list.append(pred[i][0])
    res_list.append(y_train[i][0])

l = [i for i in range(len(x_train))]    
plt.plot(l,res_list,l,plan_list)
plt.axis([0,365,0,9000])
plt.show()





