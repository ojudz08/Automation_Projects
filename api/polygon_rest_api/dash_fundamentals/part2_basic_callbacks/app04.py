'''
    DASH APP WITH MULTIPLE OUTPUTS

    So far all the callbacks we've written only update a single Output property. We can also update several outputs at once: 
        list all the properties you want to update in app.callback, and return that many items from the callback. This is particularly 
        useful if two outputs depend on the same computationally intensive intermediate result, such as a slow database query.

    A word of caution: it's not always a good idea to combine outputs, even if you can:
        If the outputs depend on some, but not all, of the same inputs, then keeping them separate can avoid unnecessary updates.
        If the outputs have the same inputs but they perform very different computations with these inputs, keeping the callbacks 
            separate can allow them to run in parallel.
'''

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
    ]),
])


@app.callback(
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('twos', 'children'),
    Output('threes', 'children'),
    Output('x^x', 'children'),
    Input('num-multi', 'value'))

def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x


if __name__ == '__main__':
    app.run_server(debug=True)
