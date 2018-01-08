# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:13:41 2018

@author: Zhong-Xun Yu
"""

from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM    # LSTM(Long-Short Term Memory)
from keras.datasets import imdb

max_features = 8000
maxlen = 88    # 設定長度為 88的字串
batch_size = 32

print("載入資料...")
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), "train sequences")
print(len(x_test), "test sequences")
print("===========================")
print(x_train[0])
print("===========================")
print('Pad sequences (sample x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)   # 取 80個 toke字彙
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)
print("===========================")
print(x_train[0])
print("===========================")
print("建立模型...")
model = Sequential()
model.add(Embedding(max_features, 128))    # 嵌入智慧
model.add(LSTM(128, dropout=0.3, recurrent_dropout=0.3))   # 128個神經元
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',      # 進行編譯
             optimizer='adam',
             metrics=['accuracy'])
print("===========================")
print('訓練和建立模型')
model.fit(x_train, y_train,
         batch_size=batch_size,
         epochs=2,
         validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test,
                           batch_size=batch_size)
print("===========================")
print('測試成績:', score)
print('測試準確度:', acc)
print("===========================")
print(model.summary())
print("===========================")
predict=model.predict_classes(x_test)
predict[0:8]
print("===========================")
predict_classes=predict.reshape(-1)    # 二維轉一維
predict_classes[0:8]
print("===========================")
PositiveDict={1:'滿意', 0:'不滿意'}
def display_info(i):
    print(x_test[i])
    print('影評真實值:', PositiveDict[y_test[i]], '; ' +'預測值:',
          PositiveDict[predict_classes[i]])
print("===========================")    
print(display_info(batch_size))