import sys
import os

def plot(x,y,size=(80,30),output_file=sys.stdout):
	#size is (rows,cols)
	canvas = _plot_canvas(size)
	for i in range(len(x)):
		xi,yi=_norm_coord(x[i],y[i],min(x),min(y),max(x),max(y),size)
		canvas[yi][xi] = '*'
	_print_canvas(canvas,output_file)

def _plot_canvas(size):
	rows,cols = size
	return [[' ' for i in range(cols)] for i in range(rows)]

def _paint_on_canvas(canvas,x,y):
	for i in range(len(x)):
		canvas[y[i]][x[i]] = '*'
	return canvas	

def _norm_coord(x,y,xmin,ymin,xmax,ymax,size):
	rows,cols = size
	len_x = float(xmax - xmin)
	len_y = float(ymax - ymin)
	xi = int(round(((x-xmin)/len_x)*(cols-1)))
	yi = int(round(((y-ymin)/len_y)*(rows-1)))
	return xi,yi

def _print_canvas(canvas,output_file):
	os.system('clear')
	for line in canvas[::-1]:
		output_file.write(''.join(line))
		output_file.write('\n')

def test_plot_canvas():
	rows,cols = (40,20)
	canvas = _plot_canvas((rows,cols))
	for i in range(rows):
		for j in range(cols):
			assert canvas[i][j] == ' '

def test_paint_on_canvas():
	rows,cols = (10,5)
	canvas = _plot_canvas((rows,cols))
	x = [0,1,2,4]
	y = [5,6,3,9]
	painted_canvas = _paint_on_canvas(canvas,x,y)
	for i in range(len(x)):
		assert painted_canvas[y[i]][x[i]] == '*'
	assert painted_canvas[4][0] == ' '

def test_norm_coord():
	rows,cols = (20,40)
	canvas = _plot_canvas((rows,cols))
	x = range(1,10)
	y = 2*x
	for i in range(len(x)):
		x[i],y[i]=_norm_coord(x[i],y[i],min(x),min(y),max(x),max(y),(rows,cols))
	assert x[0] == 0	
	assert y[0] == 0
