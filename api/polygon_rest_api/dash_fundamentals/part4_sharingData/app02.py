'''
    STORING SHARED DATA
    To share data safely across multiple processes or servers, we need to store the data somewhere that is accessible to each of the processes.

    There are three places you can store this data:
    - In the user's browser session, using dcc.Store
    - On the disk (e.g. in a file or database)
    - In server-side memory (RAM) shared across processes and servers such as a Redis database. Dash Enterprise includes onboard, one-click Redis databases for this purpose. }}

    The following examples illustrate some of these approaches.

    EXAMPLE 1 - STORING DATA IN THE BROWSWER WITH dcc.Store
    To save data in the user's browser's session:
    - The data has to be converted to a string like JSON or base64 encoded binary data for storage
    - Data that is cached in this way will only be available in the user's current session.
        - If you open up a new browser window, the app's callbacks will always re-compute the data. The data is only cached between callbacks within the same session.
        - This method doesn't increase the memory footprint of the app.
        - There could be a cost in network traffic. If you're sharing 10MB of data between callbacks, then that data will be transported over the network between each callback.
        - If the network cost is too high, then compute the aggregations upfront and transport those. Your app likely won't be displaying 10MB of data, it will just be displaying
            a subset or an aggregation of it.

    The example below shows one of the common ways you can leverage dcc.Store: if processing a dataset takes a long time and different outputs use this dataset,
        dcc.Store can be used to store the processed data as an intermediate value that can then be used as an input in multiple callbacks to generate different outputs.
        This way, the expensive data processing step is only performed once in one callback instead of repeating the same expensive computation multiple times in each callback.
    
    Notice that the data needs to be serialized into a JSON string before being placed in storage. Also note how the processed data gets stored in dcc.Store by 
        assigning the data as its output, and then the same data gets used by multiple callbacks by using the same dcc.Store as an input.
'''

app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),

    # dcc.Store stores the intermediate value
    dcc.Store(id='intermediate-value')
])

@app.callback(Output('intermediate-value', 'data'), Input('dropdown', 'value'))
def clean_data(value):
     # some expensive data processing step
     cleaned_df = slow_processing_step(value)

     # more generally, this line would be
     # json.dumps(cleaned_df)
     return cleaned_df.to_json(date_format='iso', orient='split')

@app.callback(Output('graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):

    # more generally, this line would be
    # json.loads(jsonified_cleaned_data)
    dff = pd.read_json(jsonified_cleaned_data, orient='split')

    figure = create_figure(dff)
    return figure

@app.callback(Output('table', 'children'), Input('intermediate-value', 'data'))
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    table = create_table(dff)
    return table
