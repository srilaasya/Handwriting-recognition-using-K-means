# -*- coding: utf-8 -*-
"""Model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1urwHe7y-40qSKd5IZMkdJpOn8T6TFwKt
"""

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from mlxtend.data import loadlocal_mnist
import platform

digits = datasets.load_digits()
print(digits.data)
print(digits.target)

plt.gray() 

plt.matshow(digits.images[10])

plt.show()
print(digits.target[10])

#Figure size (width, height)
fig = plt.figure(figsize=(6, 6))

#Adjust the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

#For each of the 64 images
for i in range(64):

    #Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    #Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    #Label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

plt.show()

model = KMeans(n_clusters=10, random_state=45)
model.fit(digits.data)

plt.figure(figsize=(8, 3))
plt.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

for i in range(10):
  ax = fig.add_subplot(2, 5, 1 + i, xticks=[], yticks=[])

  #Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)),  cmap=plt.cm.binary)
plt.show()

#Instead of passing a test dataset, I generated a random array by drawing 4 digits- '2131'
new_samples = np.array([
[0.00,1.07,4.80,5.34,3.97,0.00,0.00,0.00,0.00,3.05,7.62,6.40,7.63,1.60,0.00,0.00,0.00,2.29,6.41,0.99,7.62,2.29,0.00,0.00,0.00,0.00,0.00,2.36,7.62,2.14,0.00,0.00,0.00,0.00,3.81,7.47,6.48,0.30,0.00,0.00,0.00,2.52,7.62,7.47,4.42,3.59,0.15,0.00,0.00,3.58,7.62,7.62,7.24,6.64,0.46,0.00,0.00,0.15,0.76,0.61,0.00,0.00,0.00,0.00],
[0.00,3.05,6.79,2.21,0.08,0.00,0.00,0.00,0.99,7.55,7.55,7.62,7.24,2.98,0.00,0.00,2.29,7.62,1.75,2.82,6.33,7.02,0.31,0.00,4.42,7.62,0.53,0.00,2.52,7.62,1.45,0.00,5.34,7.09,0.38,0.00,2.59,7.62,1.45,0.00,2.52,7.63,6.18,3.96,7.09,6.79,0.30,0.00,0.00,3.13,6.41,6.86,5.95,1.45,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.38,0.23,0.00,0.00,0.00,0.00,0.00,0.07,6.63,4.58,2.06,0.00,0.00,0.00,0.00,1.91,7.62,5.19,7.62,0.76,0.00,0.00,0.00,4.95,7.62,5.19,7.62,6.10,2.59,0.00,0.00,6.63,7.62,7.32,7.62,5.57,1.91,0.00,0.00,0.46,0.69,2.29,7.62,1.15,0.00,0.00,0.00,0.00,0.00,1.83,7.63,1.83,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,1.22,1.52,0.61,0.00,0.00,0.00,0.00,2.44,7.62,7.62,7.63,3.74,0.00,0.00,0.00,7.17,6.25,1.83,5.57,7.24,1.60,0.00,0.00,7.62,2.06,0.00,0.76,6.94,5.34,0.00,0.00,7.62,0.30,0.00,0.69,6.79,5.34,0.00,0.00,7.62,5.34,3.81,6.33,7.32,1.60,0.00,0.00,3.97,6.86,6.86,6.63,1.98,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])

#Predicting labels
new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
