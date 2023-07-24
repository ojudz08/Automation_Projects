'''
    PASSING COMPONENTS INTO CALLBACKS INSTEAD OF IDS
    When creating app layouts in earlier examples, we assigned IDs to components within the layout and later referenced these in callback inputs and outputs.

    In the first example, there is a dcc.Input component with the id 'my-input' and a html.Div with the id 'my-output':

    You can also provide components directly as inputs and outputs without adding or referencing an id. Dash autogenerates IDs for these components.

    Below is an example. Prior to declaring the app layout, create two components, assigning each one to a variable. Then reference these variables in
        the layout and pass them directly as inputs and outputs to the callback.
    
    In Python 3.8 and higher, you can use the walrus operator to declare the component variables within the app layout

    SUMMARY
    We've covered the fundamentals of callbacks in Dash. Dash apps are built off of a set of simple but powerful principles: UIs that are 
        customizable through reactive callbacks. Every attribute/property of a component can be modified as the output of a callback, while a
        subset of the attributes (such as the value property of dcc.Dropdown component) are editable by the user through interacting with the page.
'''

from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

my_input = dcc.Input(value='initial value', type='text')
my_output = html.Div()

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        my_input        # instead of my_input var above, use --> my_input := dcc.Input(value='initial value', type='text')
    ]),
    html.Br(),
    my_output           # instead of my_output var above, use -->  my_output := html.Div() 
])


@callback(
    Output(my_output, component_property='children'),
    Input(my_input, component_property='value')
)

def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
