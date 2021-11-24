import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19,  21]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel = np.poly1d(np.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

myline = np.linspace(1, 22, 100)
# 1 is begin and 22 end

speed = mymodel(7)
print(speed)


plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
