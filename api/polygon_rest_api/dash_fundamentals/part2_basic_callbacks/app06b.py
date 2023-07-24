'''
    State allows you to pass along extra values without firing the callbacks. Below is an example but with the two dcc.Input components
        as State and a new button component as an Input.
    
    In this example, changing text in the dcc.Input boxes won't fire the callback, but clicking on the button will. The current values
        of the dcc.Input values are still passed into the callback even though they don't trigger the callback function itself.

    Note that we're triggering the callback by listening to the n_clicks property of the html.Button component. n_clicks is a property
        that gets incremented every time the component has been clicked on. It's available in every component in Dash HTML Components (dash.html),
        but most useful with buttons.
'''

# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))

def update_output(n_clicks, input1, input2):
    return f'''
        The Button has been pressed {n_clicks} times,
        Input 1 is "{input1}",
        and Input 2 is "{input2}"
    '''


if __name__ == '__main__':
    app.run_server(debug=True)
