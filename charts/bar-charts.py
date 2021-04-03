#from bokeh.plotting import Bar, output_file, show #use output_notebook to visualize it in notebook
# prepare data (dummy data)
#data = {"y": [1, 2, 3, 4, 5]}
#output_file("lines.html", title="line plot example") #put output_notebook() for notebook
#p = Bar(data, title="Line Chart Example", xlabel='x', ylabel='values', width=400, height=400)
#show(p)


from bokeh.plotting import figure, show

region = ["Global", "Asia", "Europe", "Latin America"]
volume = [3010, 1642, 716, 844]

p = figure(x_range=region)
p.vbar(x=region, top=volume, width=0.9)

show(p)