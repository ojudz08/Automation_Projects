'''
    EXAMPLE 3 - CACHING AND SIGNALING
    This example:
    - Uses Redis via Flask-Cache for storing “global variables” on the server-side in a database. This data is accessed through a function (global_store()),
        the output of which is cached and keyed by its input arguments.
    - Uses the dcc.Store solution to send a signal to the other callbacks when the expensive computation is complete.
    - Note that instead of Redis, you could also save this to the file system. See https://flask-caching.readthedocs.io/en/latest/ for more details.
    - This “signaling” is performant because it allows the expensive computation to only take up one process and be performed once. Without this type of signaling,
        each callback could end up computing the expensive computation in parallel, locking four processes instead of one.
    
    Another benefit of this approach is that future sessions can use the pre-computed value. This will work well for apps that have a small number of inputs.

    SOME THINGS TO NOTe:
    - We've simulated an expensive process by using a system sleep of 3 seconds.
    - When the app loads, it takes three seconds to render all four graphs.
    - The initial computation only blocks one process.
    - Once the computation is complete, the signal is sent and four callbacks are executed in parallel to render the graphs. Each of these callbacks
        retrieves the data from the "global server-side store": the Redis or filesystem cache.
    - We've set processes=6 in app.run_server so that multiple callbacks can be executed in parallel. In production, this is done with something like 
        $ gunicorn --workers 6 app:server. If you don't run with multiple processes, then you won't see the graphs update in parallel as callbacks will be updated serially.
    - As we are running the server with multiple processes, we set threaded to False. A Flask server can't be be both multi-process and multi-threaded.
    - Selecting a value in the dropdown will take less than three seconds if it has already been selected in the past. This is because the value is being pulled from the cache.
    - Similarly, reloading the page or opening the app in a new window is also fast because the initial state and the initial expensive computation has already been computed.

'''

import os
import copy
import time
import datetime

from dash import Dash, dcc, html, Input, Output

import numpy as np
import pandas as pd
from flask_caching import Cache


external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

CACHE_CONFIG = {
    # try 'FileSystemCache' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379')
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

N = 100

df = pd.DataFrame({
    'category': (
        (['apples'] * 5 * N) +
        (['oranges'] * 10 * N) +
        (['figs'] * 20 * N) +
        (['pineapples'] * 15 * N)
    )
})
df['x'] = np.random.randn(len(df['category']))
df['y'] = np.random.randn(len(df['category']))

app.layout = html.Div([
    dcc.Dropdown(df['category'].unique(), 'apples', id='dropdown'),
    html.Div([
        html.Div(dcc.Graph(id='graph-1'), className="six columns"),
        html.Div(dcc.Graph(id='graph-2'), className="six columns"),
    ], className="row"),
    html.Div([
        html.Div(dcc.Graph(id='graph-3'), className="six columns"),
        html.Div(dcc.Graph(id='graph-4'), className="six columns"),
    ], className="row"),

    # signal value to trigger callbacks
    dcc.Store(id='signal')
])


# perform expensive computations in this "global store"
# these computations are cached in a globally available
# redis memory store which is available across processes
# and for all time.
@cache.memoize()
def global_store(value):
    # simulate expensive query
    print(f'Computing value with {value}')
    time.sleep(3)
    return df[df['category'] == value]


def generate_figure(value, figure):
    fig = copy.deepcopy(figure)
    filtered_dataframe = global_store(value)
    fig['data'][0]['x'] = filtered_dataframe['x']
    fig['data'][0]['y'] = filtered_dataframe['y']
    fig['layout'] = {'margin': {'l': 20, 'r': 10, 'b': 20, 't': 10} }
    return fig


@app.callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_value(value):
    # compute value and send a signal when done
    global_store(value)
    return value


@app.callback(Output('graph-1', 'figure'), Input('signal', 'data'))
def update_graph_1(value):
    # generate_figure gets data from `global_store`.
    # the data in `global_store` has already been computed
    # by the `compute_value` callback and the result is stored
    # in the global redis cached
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}
            }
        }]
    })


@app.callback(Output('graph-2', 'figure'), Input('signal', 'data'))
def update_graph_2(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'lines',
            'line': {'shape': 'spline', 'width': 0.5},
        }]
    })


@app.callback(Output('graph-3', 'figure'), Input('signal', 'data'))
def update_graph_3(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2d',
        }]
    })


@app.callback(Output('graph-4', 'figure'), Input('signal', 'data'))
def update_graph_4(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2dcontour',
        }]
    })


if __name__ == '__main__':
    app.run_server(debug=True, processes=6, threaded=False)
