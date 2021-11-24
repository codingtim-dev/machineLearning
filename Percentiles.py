####Percentiles in PY###

import numpy as np
import matplotlib.pyplot as plt


ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x = np.percentile(ages, 75)
y = np.percentile(ages, 90)

# get the percentile value of the ages which are lower than the 75 % or 90%

print(x)
print(x)

# plt.hist(x, 10)
# plt.show()

# plt.hist(y, 2)
# plt.show()




