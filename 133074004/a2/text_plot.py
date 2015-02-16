from plot import plot
plot()

import math
from plot import sin_func
assert sin_func(math.pi/2,1) == 1
assert sin_func(math.pi/4,10) == 7
assert sin_func(math.pi/8,10) == 4
assert sin_func(-math.pi/8,10) == -4 
assert sin_func(2*math.pi,1) == 0
assert sin_func(3*math.pi/2,1) == -1 

from plot import normalized_coordinates
assert normalized_coordinates(1,1,1,1) == (0,2)

