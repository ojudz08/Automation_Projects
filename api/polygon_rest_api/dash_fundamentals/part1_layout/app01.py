'''
    DASH LAYOUT
    This tutorial will walk you through a fundamental aspect of Dash apps, the app layout, through six self-contained apps.
    For production Dash apps, we recommend styling the app layout with Dash Enterprise Design Kit.
    Dash apps are composed of two parts. The first part is the "layout", which describes what the app looks like. The second part 
        describes the interactivity of the app and will be covered in the next chapter.
    
    Note:
    1. The layout is composed of a tree of "components" such as html.Div and dcc.Graph.
    2. The Dash HTML Components module (dash.html) has a component for every HTML tag. The html.H1(children='Hello Dash') component
        generates a <h1>Hello Dash</h1> HTML element in your app.
    3. Not all components are pure HTML. The Dash Core Components module (dash.dcc) contains higher-level components that are interactive
        and are generated with JavaScript, HTML, and CSS through the React.js library.
    4. Each component is described entirely through keyword attributes. Dash is declarative: you will primarily describe your app through these attributes.
    5. The children property is special. By convention, it's always the first attribute which means that you can omit it: 
        html.H1(children='Hello Dash') is the same as html.H1('Hello Dash'). It can contain a string, a number, a single component, or a list of components.
    6. The fonts in your app will look a little bit different than what is displayed here. This app is using a custom CSS stylesheet and Dash Enterprise Design Kit to modify the default styles of the elements. You can learn more about custom CSS in the CSS tutorial.
'''


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)