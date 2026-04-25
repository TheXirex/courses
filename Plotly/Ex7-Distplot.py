#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: 'data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

# create a DataFrame from the .csv file:
df = pd.read_csv('data/iris.csv')

# Define the traces
# HINT:
# This grabs the petal_length column for a particular flower
# df[df['class']=='Iris-some-flower-class']['petal_length']
trace1 = df[df['class']=='Iris-setosa']['petal_length']
trace2 = df[df['class']=='Iris-versicolor']['petal_length']
trace3 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
hist_data = [trace1, trace2, trace3]
group_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='distplot_exercise.html')
