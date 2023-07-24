'''
    MORE ABOUT HTML COMPONENTS

    Dash HTML Components (dash.html) contains a component class for every HTML tag as well as keyword arguments for all of the HTML arguments.

    In this example, we modified the inline styles of the html.Div and html.H1components with the style property.
        html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'})

    The above code is rendered in the Dash app as <h1 style="text-align: center; color: #7FDBFF">Hello Dash</h1>.

    There are a few important differences between the dash.html and the HTML attributes:
    1. The style property in HTML is a semicolon-separated string. In Dash, you can just supply a dictionary.
    2.The keys in the style dictionary are camelCased. So, instead of text-align, it's textAlign.
    3. The HTML class attribute is className in Dash.
    4. The children of the HTML tag is specified through the children keyword argument. By convention, this is always the first argument and so it is often omitted.

    Besides that, all of the available HTML attributes and tags are available to you within your Python context.

'''


# Customize the text in the app by modifying the inline styles of the components.

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', 
             style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)