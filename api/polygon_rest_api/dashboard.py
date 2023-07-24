import config
import pandas as pd
import requests
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Set your API key and endpoint
API_KEY = config.api_key
API_ENDPOINT = 'https://api.polygon.io/v2/aggs/ticker/{}/range/1/day/{}/{}?apiKey={}'

# Define the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Stock Prices'),
    dcc.Input(id='input', value='AAPL', type='text'),
    html.Div(id='output-graph')
])

# Define the callback
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(ticker):
    # Get the data from the API
    url = API_ENDPOINT.format(ticker, '2010-01-01', '2023-04-17', API_KEY)
    response = requests.get(url)
    data = response.json()['results']

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.set_index('timestamp')

    # Create the chart
    fig = {
        'data': [{'x': df.index, 'y': df['close'], 'type': 'line'}],
        'layout': {'title': ticker}
    }

    # Return the chart
    return dcc.Graph(id='example-graph', figure=fig)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
