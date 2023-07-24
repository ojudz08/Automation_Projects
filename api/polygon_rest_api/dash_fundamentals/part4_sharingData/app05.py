'''
    EXAMPLE 4 - USER-BASED SESSION DATA ON THE SERVER
    The previous example cached computations in a way that was accessible for all users.

    Sometimes you may want to keep the data isolated to user sessions: one user's derived data shouldn't update the next user's derived data. 
        One way to do this is to save the data in a dcc.Store, as demonstrated in the first example.

    Another way to do this is to save the data in a cache along with a session ID and then reference the data using that session ID. Because data is
        saved on the server instead of transported over the network, this method is generally faster than the dcc.Store method.

    This method was originally discussed in a Dash Community Forum thread.
    This example:
    - Caches data using the flask_caching filesystem cache. You can also save to an in-memory cache or database such as Redis instead.
    - Serializes the data as JSON.
        - If you are using Pandas, consider serializing with Apache Arrow for faster serialization or Plasma for smaller dataframe size. Community thread
    - Saves session data up to the number of expected concurrent users. This prevents the cache from being overfilled with data.
    - Creates unique session IDs for each session and stores it as the data of dcc.Store on every page load. This means that every user session 
        has unique data in the dcc.Store on their page.

    THREE THINGS:
    - The timestamps of the dataframe don't update when we retrieve the data. This data is cached as part of the user's session.
    - Retrieving the data initially takes three seconds but successive queries are instant, as the data has been cached.
    - The second session displays different data than the first session: the data that is shared between callbacks is isolated to individual user sessions.
'''

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import datetime
from flask_caching import Cache
import os
import pandas as pd
import time
import uuid

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    # Note that filesystem cache doesn't work on systems with ephemeral
    # filesystems like Heroku.
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',

    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 200
})


def get_dataframe(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/session-unique data processing step goes here

        # simulate a user/session-unique data processing step by generating
        # data that is dependent on time
        now = datetime.datetime.now()

        # simulate an expensive data processing task by sleeping
        time.sleep(3)

        df = pd.DataFrame({
            'time': [
                str(now - datetime.timedelta(seconds=15)),
                str(now - datetime.timedelta(seconds=10)),
                str(now - datetime.timedelta(seconds=5)),
                str(now)
            ],
            'values': ['a', 'b', 'a', 'c']
        })
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))


def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        dcc.Store(data=session_id, id='session-id'),
        html.Button('Get data', id='get-data-button'),
        html.Div(id='output-1'),
        html.Div(id='output-2')
    ])


app.layout = serve_layout


@app.callback(Output('output-1', 'children'),
              Input('get-data-button', 'n_clicks'),
              Input('session-id', 'data'))
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 1 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


@app.callback(Output('output-2', 'children'),
              Input('get-data-button', 'n_clicks'),
              Input('session-id', 'data'))
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 2 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
