'''
    DASH APP LAYOUT WITH FIGURE AND SLIDER

    In this example, the "value" property of the dcc.Slider is the input of the app, and the output of the app is the "figure" property 
        of the dcc.Graph. Whenever the value of the dcc.Slider changes, Dash calls the callback function update_figure with the new value.
        The function filters the dataframe with this new value, constructs a figure object, and returns it to the Dash application.

    There are a few nice patterns in this example:
    1. We use the Pandas library to load our dataframe at the start of the app: df = pd.read_csv('...'). This dataframe df 
        is in the global state of the app and can be read inside the callback functions.
    2. Loading data into memory can be expensive. By loading querying data at the start of the app instead of inside the callback functions, 
        we ensure that this operation is only done once -- when the app server starts. When a user visits the app or interacts with the app, 
        that data (df) is already in memory. If possible, expensive initialization (like downloading or querying data) should be done in the 
        global scope of the app instead of within the callback functions.
    3. The callback does not modify the original data, it only creates copies of the dataframe by filtering using pandas. This is important: 
        your callbacks should never modify variables outside of their scope. If your callbacks modify global state, then one user's session 
        might affect the next user's session and when the app is deployed on multiple processes or threads, those modifications will not be 
        shared across sessions.
    4. We are turning on transitions with layout.transition to give an idea of how the dataset evolves with time: transitions allow the chart
        to update from one state to the next smoothly, as if it were animated.
'''

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))

def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)
    
    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)