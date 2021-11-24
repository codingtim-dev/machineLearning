import numpy as np
import matplotlib.pyplot as plt

# generate random data sets of any size

x = np.random.uniform(0.0, 5.0, 250)    # contains 250 values between 0 and 5

# print(x)

plt.hist(x, 5)
# shows how many values are between 0 & 1, 1 & 2, 2 & 3, ...
plt.show()

# create a BIG data distribution

x = np.random.uniform(0.0, 5.0, 10000)

plt.hist(x, 100)
# shows all x-values in 100 bars
plt.show()
