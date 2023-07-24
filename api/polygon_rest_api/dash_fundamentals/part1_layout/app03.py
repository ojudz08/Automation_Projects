'''
    REUSABLE COMPONENTS
    By writing our markup in Python, we can create complex reusable components like tables without switching contexts or languages.
'''
# Example that generates a Table from Pandas dataframe

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(dfInput, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dfInput.columns])
        ),

        html.Tbody([
            html.Tr([
                html.Td(dfInput.iloc[i][col]) for col in dfInput.columns
            ]) for i in range(min(len(dfInput), max_rows))
        ])
    ])

app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)