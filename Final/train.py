import csv
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

RANDOM_SEED = 42
# 路徑指定
dataset = 'pose10.csv'
model_save_path = 'pose021.hdf5'
# 分類數指定
NUM_CLASSES = 4
# 學習數據
# loadtxt:抓文本/自訂變數:dataset:路徑/delimiter用,分開/dtype:數據類型/ usecols:設定形狀，載入第一列到第42列
# 特徵
X_dataset = np.loadtxt(dataset, delimiter=',', dtype='float32', usecols=list(range(1, 42+ 1)))
# 分類
y_dataset = np.loadtxt(dataset, delimiter=',', dtype='int32', usecols=(0))
# 分割訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X_dataset, y_dataset, train_size=0.75, random_state=RANDOM_SEED)

# 訓練模型
# 一個輸入層、兩個隱藏層和一個輸出層
model = tf.keras.models.Sequential([
    tf.keras.layers.Input((42, )),
    #tf.keras.layers.Dropout(0.05),
    tf.keras.layers.Dense((42//2)+1, activation='relu'),
    #tf.keras.layers.Dropout(0.05),
    tf.keras.layers.Dense((42//4)+1, activation='relu'),
    tf.keras.layers.Dense(NUM_CLASSES, activation='softmax')
])

# 模型檢查點回調
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    model_save_path, verbose=1, save_weights_only=False)
# 早期終止用回撥函數
es_callback = tf.keras.callbacks.EarlyStopping(patience=20, verbose=1)

# 模型編譯
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 模型訓練
model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=90,
    validation_data=(X_test, y_test),
    callbacks=[cp_callback, es_callback]
)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

def print_confusion_matrix(y_true, y_pred, report=True):
    labels = sorted(list(set(y_true)))
    cmx_data = confusion_matrix(y_true, y_pred, labels=labels)
    sns.set(font_scale=1)
    df_cmx = pd.DataFrame(cmx_data, index=labels, columns=labels)
 
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(df_cmx, annot=True, fmt='g' ,square=False)
    ax.set_ylim(len(set(y_true)), 0)
    plt.show()
    
    if report:
        print('Classification Report')
        print(classification_report(y_test, y_pred))

Y_pred = model.predict(X_test)
y_pred = np.argmax(Y_pred, axis=1)

print_confusion_matrix(y_test, y_pred)