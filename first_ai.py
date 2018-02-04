from sklearn import datasets 

house_price = datasets.load_boston()
digits = datasets.load_digits()
print(digits.images[0])