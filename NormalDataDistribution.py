### is known as the Gaussian data distribution

import numpy as np
import matplotlib.pyplot as plt

# mean value is 5.0 and standard deviation is 1.0
# --> most values are between 4.0 and 6.0

x = np.random.normal(5.0, 1.0, 100000)

# result called bell curve
plt.hist(x, 100)
plt.show()
