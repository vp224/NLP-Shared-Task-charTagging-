from keras.models import Sequential
from keras import layers
import numpy as np
from keras.models import load_model

X = []
Y = []
with open('./sans.txt') as f:
    for line in f:
        x = "...."+line.strip()
        for i in range(len(x)-4):
            y = x[i:i+5]
            temp = []
            for j in range(5):
                a = ord(y[j].lower())
                if a==46:
                    temp.append(0)
                elif a==32:
                    temp.append(100)
                else:
                    temp.append(((a-97)*2)+1)
            X.append(temp)
            a = ord(y[4])
            if a>96:
                Y.append([((a-97)*2)+1])
            elif a==32:
                Y.append([100])
            else:
                Y.append([((a-65)*2)+2])
print len(X),len(Y),len(X[0]),len(Y[0])

sp = int(0.8*len(X))
X = X[0:sp]
Y = Y[0:sp]

X_train = np.array(X).reshape(len(X),1,5)
y_train = np.array(Y).reshape(len(Y),1,1)

model=Sequential()
model.add(layers.LSTM(units=10,return_sequences = True,stateful=True,batch_input_shape=(1,1,5)))
model.add(layers.LSTM(units=5,return_sequences = True,stateful=True,batch_input_shape=(1,1,10)))
model.add(layers.LSTM(units=1,return_sequences = True,stateful=True,batch_input_shape=(1,1,5)))
model.add(layers.Dense(1))
model.compile(loss = "mse", optimizer = "rmsprop")
model.fit(X_train, y_train, epochs = 2, batch_size = 1)

model.save('./saved_model_2.h5')
