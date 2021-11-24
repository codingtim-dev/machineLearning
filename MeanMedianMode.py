####MACHINE LEARNING IN PY####

import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = np.mean(speed)      #gets the Mean value (average)

print(x)

x = np.median(speed)       #in sorted order gets the value in the middle

print(x)

x = stats.mode(speed)       #find the number that appears the most

print(x)
