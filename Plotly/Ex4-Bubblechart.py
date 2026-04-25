#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df = pd.read_csv('data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
# Let's use horsepower for x, mpg for y, and weight for bubble size
# Weight numbers are large, so we should scale them down for the marker size
data = [go.Scatter(
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(
        size=df['weight'] / 100,
        color=df['cylinders'],
        showscale=True
    )
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title='Vehicle MPG vs Horsepower',
    xaxis=dict(title='Horsepower'),
    yaxis=dict(title='MPG'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_exercise.html')
