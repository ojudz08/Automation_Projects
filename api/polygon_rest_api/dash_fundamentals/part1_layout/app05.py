'''
    MARKDOWN
    While Dash exposes HTML through Dash HTML Components (dash.html), it can be tedious to write your copy in HTML. 
        For writing blocks of text, you can use the Markdown component in Dash Core Components (dash.dcc). 
'''

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc

app = Dash(__name__)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/) if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug=True)