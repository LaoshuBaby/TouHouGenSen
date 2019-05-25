import tensorflow as tf
w = tf.Variable(tf.random_normal([100, 1]))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    a = sess.run(w)
    print("平均值" + str(sess.run(tf.reduce_mean(w))))
    print("最大值" + str(a[sess.run(tf.math.argmax(w, 0))]))
    print("最小值" + str(a[sess.run(tf.math.argmin(w, 0))]))
