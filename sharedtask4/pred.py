from keras.models import Sequential
from keras import layers
import numpy as np
from keras.models import load_model

model = load_model('saved_model_2.h5')
with open('./inp2','w') as f2:
    with open('./out2','w') as f1:
        with open('./sans.txt') as f:
            lines = f.readlines()[353378:]
            for line in lines:
                x = "...."+line.strip()
                X = []
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
                X = np.array(X).reshape(len(X),1,5)
                Y = model.predict(X,batch_size=1)
                Y = model.predict(X,batch_size=1)
                for i in range(len(Y)):
                    a = int(Y[i][0][0])
                    if X[i][0][4]<53:
                        if a==X[i][0][4] or a==X[i][0][4]+1:
                            if a%2==0:
                                f1.write(unichr(64+(a/2)))
                            else:
                                f1.write(unichr(96+((a+1)/2)))
                        else:
                            f1.write(unichr(96+((X[i][0][4]+1)/2)))
                    else:
                        f1.write(' ')
                f1.write('\n')
                f2.write(line)
