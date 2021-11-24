####MACHINE LEARNING IN PY####

import numpy as np

speed = [86, 87, 88, 86, 87, 85, 86]

x = np.std(speed)                #gets the standard deviation ,  means how spread out the most numbers are 
                                   
print(x)


speed2 = [32, 111, 138, 28, 59, 77, 97]     #gets the variance of the values

x = np.var(speed2)

print(x)

