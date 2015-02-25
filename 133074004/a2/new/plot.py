import sys

def _make_canvas(size):
	cols, rows = size
	canvas = []
	for i in range(0,rows):
		canvas.append(list(' '*cols))
	return canvas

def _map_point(x,y,xmin,xmax,ymin,ymax,size):
	x_len = xmax - xmin
	y_len = ymax - ymin
	

def plot(x,y,size=(80,30),output_file=sys.stdout):
	xmin, xmax = min(x), max(x)
	ymin, ymax = min(y), max(y)

def test_plot():
	x = [0,1]
	y = [0,1]
	plot(x,y)

def test_make_canvas():
	size = (6,5)
	canvas = make_canvas(size)	
	assert len(canvas) == size[1]
	assert len(canvas[0]) == size[0]
	for i in range(0, size[1]):
		for j in range(0, size[0]):
			assert canvas[i][j] == ' '
		
	
