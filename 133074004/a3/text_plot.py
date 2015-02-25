from plot import plot
import math

size = (30,80)
points = 80
x,y = [],[]
for i in range(points):
	x.append(2*i*math.pi/(points-1))
	y.append(math.sin(x[i]))
plot(x,y)
