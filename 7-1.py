import tensorflow as tf
import tensorflow.keras.datasets as ds
import matplotlib.pyplot as plt

(X_train, y_train),(X_test, y_test) = ds.mnist.load_data()
print(X_train.shape(),y_train.shape(),X_test.shape(),y_test.shape())
plt.figure(figsize=(4,3))
plt.suptitle('MNIST',fontsize=30)
for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(X_train[i],cmap='gray')
    plt.xticks([]);plt.yticks([])
    plt.title(str(y_train[i]),fontsize=30)
    
(X_train, y_train),(X_test, y_test) = ds.cifar10.load_data()
print(X_train.shape(),y_train.shape(),X_test.shape(),y_test.shape())
class_names = ['airplane','car','bird','cat','deer','dog','frog','horse','ship','truck']
plt.figuresize(figsize=(24,3))
for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(X_train[i])
    plt.xticks([]);plt.yticks([])
    plt.title(class_names[y_train[i,0]],fontsize=30)