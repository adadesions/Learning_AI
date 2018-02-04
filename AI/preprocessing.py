import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])

data_binerize = preprocessing.Binarizer(threshold=0).transform(input_data)
print(data_binerize)

print('\nBefore:')
print('Mean=', input_data.mean(axis=0))
print('Std=', input_data.std(axis=0))

print('\nAfter')
data_scaled = preprocessing.scale(input_data)
print('Mean=', data_scaled.mean(axis=0))
print('Std=', data_scaled.std(axis=0))

data_l1 = preprocessing.normalize(input_data, norm='l1')
data_l2 = preprocessing.normalize(input_data, norm='l2')

print('L1 Normalize\n', data_l1)
print('L2 Normalize\n', data_l2)
