# coding=utf-8

import pandas
import bokeh.charts

df = pandas.read_excel("verlegenhuken.xlsx", sheetname=0)
df["Temperature"] = df["Temperature"]/10
df["Pressure"] = df["Pressure"]/10

bokeh.charts.output_file("Temp_Pressure_chart.html")

plot = bokeh.charts.Scatter(df, x="Temperature", y="Pressure",
                            title="Temperature and air Pressure",
                            xlabel="Temperature", ylabel="Pressure")

bokeh.charts.show(plot)

import bokeh.plotting

plot = bokeh.plotting.Figure(plot_width=800, plot_height=800,
                             title="Temperature and air pressure")
plot.circle(df["Temperature"], df["Pressure"], size=2, color="blue", alpha=0.8)
plot.xaxis.axis_label = "Temperature"
plot.yaxis.axis_label = "Pressure"
bokeh.plotting.output_file("Temp_pressure_plotting.html")

bokeh.plotting.show(plot)