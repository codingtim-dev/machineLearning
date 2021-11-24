####shows the popultion of magdeburg 1800 - 2018

import pandas
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
from sklearn.metrics import r2_score


df = pandas.read_csv('PopulationMD.csv')


plt.xlabel('Year')
plt.ylabel('Population')

X = df[['Year']]
y = df[['Population']]

#mymodel = np.poly1d(np.polyfit(X, y, 3))

#print(r2_score(y, mymodel(X)))


#regr = linear_model.LinearRegression()
#regr.fit(X, y)

plt.plot(X  ,  y, "b--")
plt.title("Population of Magdeburg 1800 -")
plt.show()
