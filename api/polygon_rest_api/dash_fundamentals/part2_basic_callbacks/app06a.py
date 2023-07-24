'''
    DASH APP WITH STATE
    In some cases, you might have a "form"-like pattern in your application. In such a situation, you may want to read the
    value of an input component, but only when the user is finished entering all of their information in the form rather than immediately after it changes.

    In this example, the callback function is fired whenever any of the attributes described by the Input change.
'''

# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-1", type="text", value="Montréal"),
    dcc.Input(id="input-2", type="text", value="Canada"),
    html.Div(id="number-output"),
])


@app.callback(
    Output("number-output", "children"),
    Input("input-1", "value"),
    Input("input-2", "value"),
)

def update_output(input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)


if __name__ == "__main__":
    app.run_server(debug=True)
