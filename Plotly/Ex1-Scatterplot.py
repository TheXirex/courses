#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np


# Define a data variable
np.random.seed(42)
random_x = np.random.randn(1000)
random_y = np.random.rand(1000)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]


# Define the layout
layout = go.Layout(
    title = 'Random Data Scatterplot',
    xaxis = dict(title = 'Normal Distribution'),
    yaxis = dict(title = 'Uniform Distribution'),
    hovermode = 'closest'
)


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter_exercise.html')
