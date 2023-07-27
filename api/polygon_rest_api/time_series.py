from pathlib import Path
import os, sys
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px




def read_data(src_file):
    df = pd.read_csv(src_file)
    return df


def create_time_series(data):
    fig = px.scatter(data, x='Date', y='Open')
    fig.show()
    return fig



if __name__ == '__main__':
    project_folder = os.path.join(Path(__file__).parents[0], 'ohlc_data')
    filename = r'test.csv'
    src_file = os.path.join(project_folder, filename)
    
    data = read_data(src_file)
    
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    fig.show()