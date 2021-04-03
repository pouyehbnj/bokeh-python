import numpy as np
from bokeh.io import show, output_file
from bokeh.plotting import figure

data = np.random.normal(0, 0.5, 1000)
hist, edges = np.histogram(data, density=True, bins=50)

p = figure()
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white")

output_file("histogram.html")
show(p)