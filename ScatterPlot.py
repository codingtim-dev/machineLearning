import matplotlib.pyplot as plt
import numpy as np

# scatter shows dots

y = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
x = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# x represents the speed of each car
# y represents the age of each car

plt.scatter(x, y)
plt.show()

# random data distribution

x = np.random.normal(5.0, 1.0, 10000)
y = np.random.normal(10.0, 2.0, 10000)

plt.scatter(x, y)
plt.show()