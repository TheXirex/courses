#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    html.Div([
        html.Label("Input 1:"),
        dcc.Input(id='input-1', type='number', value=1, style={'margin-right': '20px'}),
        
        html.Label("Input 2:"),
        dcc.Input(id='input-2', type='number', value=1)
    ], style={'padding': '20px'}),
    
    html.H3("Product:", style={'padding': '0 20px'}),
    html.Div(id='output-product', style={'padding': '0 20px', 'font-size': '24px', 'font-weight': 'bold'})
])

# Create a Dash callback:
@app.callback(
    Output('output-product', 'children'),
    [Input('input-1', 'value'),
     Input('input-2', 'value')]
)
def update_output(num1, num2):
    # Handle cases where input might be empty
    if num1 is None or num2 is None:
        return "Please provide both numbers"
    
    product = num1 * num2
    return f"{num1} * {num2} = {product}"

# Add the server clause:
if __name__ == '__main__':
    app.run_server()
