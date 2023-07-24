'''
    BASIC DASH CALLBACKS

    In the previous chapter we learned that app.layout describes what the app looks like and is a hierarchical tree of 
        components. The Dash HTML Components (dash.html) module provides classes for all of the HTML tags, and the keyword
        arguments describe the HTML attributes like style, className, and id. The Dash Core Components (dash.dcc) module 
        generates higher-level components like controls and graphs.

    This chapter describes how to make your Dash apps using callback functions: functions that are automatically called 
        by Dash whenever an input component's property changes, in order to update some property in another component (the output).

    For optimum user-interaction and chart loading performance, production Dash apps should consider the Job Queue, HPC, 
        Datashader, and horizontal scaling capabilities of Dash Enterprise.


    SIMPLE INTERACTIVE DASH APP

    Let's break down this example:
    The "inputs" and "outputs" of our application are described as the arguments of the @app.callback decorator.
    
    Learn more about using the @app.callback decorator.
        In Dash, the inputs and outputs of our application are simply the properties of a particular component. In this example,
            our input is the "value" property of the component that has the ID "my-input". Our output is the "children" property 
            of the component with the ID "my-output".
        
        Whenever an input property changes, the function that the callback decorator wraps will get called automatically. Dash 
            provides this callback function with the new value of the input property as its argument, and Dash updates the property
            of the output component with whatever was returned by the function.

        The component_id and component_property keywords are optional (there are only two arguments for each of those objects). They 
            are included in this example for clarity but will be omitted in the rest of the documentation for the sake of brevity and readability.
        
        Don't confuse the dash.dependencies.Input object and the dcc.Input object. The former is just used in these callback definitions and the 
            latter is an actual component. Notice how we don't set a value for the children property of the my-output component in the layout. 
            When the Dash app starts, it automatically calls all of the callbacks with the initial values of the input components in order to populate
            the initial state of the output components. In this example, if you specified the div component as html.Div(id='my-output', children='Hello world'), 
            it would get overwritten when the app starts.

    It's sort of like programming with Microsoft Excel: whenever a cell changes (the input), all the cells that depend on that cell (the outputs) will 
        get updated automatically. This is called "Reactive Programming" because the outputs react to changes in the inputs automatically.

    Remember how every component is described entirely through its set of keyword arguments? Those arguments that we set in Python become properties
        of the component, and these properties are important now. With Dash's interactivity, we can dynamically update any of those properties using 
        callbacks. Often we'll update the children property of HTML components to display new text (remember that children is responsible for the contents
        of a component) or the figure property of a dcc.Graph component to display new data. We could also update the style of a component or even the available
        options of a dcc.Dropdown component!
'''

from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)

def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
