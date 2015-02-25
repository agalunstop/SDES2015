from plot import plot
plot()

import math
#from plot import sin_func
assert sin_func(math.pi/2,1) == 1
assert sin_func(math.pi/4,10) == 7
assert sin_func(math.pi/8,10) == 4
assert sin_func(-math.pi/8,10) == -4 
assert sin_func(2*math.pi,1) == 0
assert sin_func(3*math.pi/2,1) == -1 

from plot import normalized_coordinates
assert normalized_coordinates(1,1,1,1) == (0,2)

def sin_func(angle,mult_factor):
    import math
    return int(round(mult_factor*math.sin(angle)))

def sin_plot_values(rows,cols):
    import math
    sin_dict = []
    for i in range(cols):
        sin_dict.append(sin_func(2*i*math.pi/(cols-1),rows/2))
    return sin_dict
