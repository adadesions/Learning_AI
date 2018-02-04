import numpy as np
from sklearn import preprocessing

input_label = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']
encoder = preprocessing.LabelEncoder()
encoder.fit(input_label)

print('Label Mapping')
for i, item in enumerate(encoder.classes_):
    print(item, '-->', i)

test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print('\nLabels = ', test_labels)
print('Encoded value', list(encoded_values))
decoded_list = encoder.inverse_transform(encoded_values)
print('Decoded value', list(decoded_list))