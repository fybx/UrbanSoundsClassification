import cv2 as cv
import os
import pandas as pd

X = []
Y = []
for path, subdirs, files in os.walk("C:/Users/skili/Desktop/python for globalia/spectrograms"):
    for name in files:
        file = os.path.join(path, name)
        spectrogram = cv.imread(file, 0)
        spectrogram = spectrogram / 255
        X.append(spectrogram)
        Y.append(file.split('/')[4])



len(X)

len(Y)

X_train = X[0:6900]

Y_train = Y[0:6900]

train = pd.DataFrame()
train["X_train"] = X_train
train["Y_train"] = Y_train
train.to_csv("train.csv")

X_val = X[6900:7800]
Y_val = Y[6900:7800]

validation = pd.DataFrame()
validation["X_val"] = X_val
validation["Y_val"] = Y_val
validation.to_csv("validation.csv")

X_test = X[7800:8735]
Y_test = Y[7800:8735]

test = pd.DataFrame()
test["X_test"] = X_test
test["Y_test"] = Y_test
test.to_csv("test.csv")

