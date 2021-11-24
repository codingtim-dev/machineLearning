#### this script will showing the average phone using time
#### data collecting started at the 8th february 2020
#### represent also the distribution of male and female

import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pandas.read_csv('APUT.csv')

X = df[['Age']]
y = df[['APUT']]

regr = linear_model.LinearRegression()
regr.fit(X, y)

plt.scatter(X, y)
plt.show()

