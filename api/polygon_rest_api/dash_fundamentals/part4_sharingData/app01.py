'''
    Here is a sketch of an app that will not work reliably because the callback modifies a global variable, which is outside of its scope.
'''

df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
	dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@app.callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
	global df
	df = df[df['score'] == value]
	return len(df)


'''
    The callback returns the correct output the very first time it is called, but once the global df variable is modified, any subsequent callback that
        uses that dataframe is not using the original data anymore.

    To improve this app, reassign the filtered dataframe to a new variable inside the callback as shown below, or follow one of the strategies outlined in the next parts of this guide.
'''

df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
    dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@app.callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
	filtered_df = df[df['score'] == value]
	return len(filtered_df)
