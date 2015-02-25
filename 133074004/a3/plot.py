import sys
import os

class plot_obj(object):
	"""Class to draw a plot with given x and y tuples"""
	def __init__(self,x,y,size):
		self.rows,self.cols = size
		self.xmin = min(x)
		self.xmax = max(x)
		self.ymin = min(y)
		self.ymax = max(y)
		self.len_x = float(self.xmax-self.xmin)
		self.len_y = float(self.ymax-self.ymin)
		self.x = x
		self.y = y
		self.canvas = []
		self.xnorm = []
		self.ynorm = []
	def make_canvas(self):
		self.canvas = [[' ' for i in range(self.cols)] for i in range(self.rows)]
	def norm_coord(self):
		for i in range(len(self.x)):
			self.xnorm.append(int(round(((self.x[i]-self.xmin)/self.len_x)\
			*(self.cols-1))))	
			self.ynorm.append(int(round(((self.y[i]-self.ymin)/self.len_y)\
			*(self.rows-1))))	
	def paint_on_canvas(self):
		for i in range(len(self.xnorm)):
			self.canvas[self.ynorm[i]][self.xnorm[i]] = '*'
	def print_canvas(self,output_file=sys.stdout):
		import os
		os.system('clear')
		for line in self.canvas[::-1]:
			output_file.write(''.join(line))
			output_file.write('\n')
		
####### End of Class #################

#def plot(x,y,size=(80,30),output_file=sys.stdout):
	#size is (rows,cols)
import numpy

def plot(x,y,size=(30,80),output_file=sys.stdout):
#	from plot import plot_obj
	p = plot_obj(x,y,size)
	p.make_canvas()
	p.norm_coord()
	p.paint_on_canvas()
	p.print_canvas()
