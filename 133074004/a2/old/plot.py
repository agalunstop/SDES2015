#text based plotter
def plot(cols=81,rows=31):
    import os
#   x,y = rounded(x,y)

    initial_plot = list_of_spaces(cols,rows)
    x_axis_index,y_axis_index,axes_plot = plot_axes(cols,rows,initial_plot)
#   print x,y
    sin_list =  sin_plot_values(rows-1,cols-1)
#   print sin_list
    final_plot = axes_plot
    for i in range(len(sin_list)-1):
        row,col = normalized_coordinates(i,sin_list[i],x_axis_index,y_axis_index)
        final_plot = change_index_xy_to_star(row,col,final_plot)

    os.system('clear')
    print_plot(final_plot)

def normalized_coordinates(x,y,x_axis_index,y_axis_index):
    row = int(x_axis_index-y)
    col = int(y_axis_index+x)
    return row,col

#round and convert to integer
def rounded(x,y):
    return int(round(x)),int(round(y))

#plot x and y axes in a given array
def plot_axes(cols,rows,plot):
    x_axis_index = int(rows/2)
#   y_axis_index = int(cols/2)
    y_axis_index = 0
    for i in range(cols):
        plot[x_axis_index][i] = '-'
    for i in range(rows):
        plot[i][y_axis_index] = '|'
    return x_axis_index,y_axis_index,plot

#create an array of given spaces of given size
def list_of_spaces(x,y):
    return [[' ' for i in range(x)] for i in range(y)]      #2D array of x columns y rows

#write star at the index given in a twod array
def change_index_xy_to_star(row,col,twod_list):
    twod_list[row][col] = '*'
    return twod_list

#print the given array as a plot
def print_plot(twod_list):
    import sys
    for row in twod_list:
        for col in row:
            sys.stdout.write(col)                           #printing without spaces or newline
        print

def sin_func(angle,mult_factor):
    import math
    return int(round(mult_factor*math.sin(angle)))

def sin_plot_values(rows,cols):
    import math
    sin_dict = []
    for i in range(cols):
        sin_dict.append(sin_func(2*i*math.pi/(cols-1),rows/2))
    return sin_dict

