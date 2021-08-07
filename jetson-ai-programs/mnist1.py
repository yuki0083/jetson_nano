import tensorflow as tf
from tensorflow.keras import callbacks

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#モデルの構築
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

#損失関数のオブジェクト
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

#訓練用のモデルを構成
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

"""tensorboard"""
#logの保存場所
log_filepath = "./logs/"
tb_cb = tf.keras.callbacks.TensorBoard(log_dir=log_filepath, histogram_freq=1)

#訓練
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), callbacks=[tb_cb])
#評価
model.evaluate(x_test,  y_test)
#保存
model.save('mnist.hd5')