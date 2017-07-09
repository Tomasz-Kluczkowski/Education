# coding=utf-8
from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%d-%m-%Y %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%d-%m-%Y %H:%M:%S")

cds = ColumnDataSource(df)
p = figure(x_axis_type="datetime", height=100, width=500, responsive=True,
           title="Motion Graph")
hover = HoverTool(tooltips=[("Start", "@Start_string"),
                            ("End", "@End_string")])
p.add_tools(hover)
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

q = p.quad(left="Start", right="End", bottom=0, top=1,
           color="green", source=cds)
output_file("Graph.html")
show(p)