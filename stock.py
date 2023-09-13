import datetime
import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Stock Market Analysis'),

    dcc.Input(id='input-ticker', type='text', value='GOOGL'),
    html.Div(id='output-graph')
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    Input(component_id='input-ticker', component_property='value')
)
def update_graph(input_value):
    # Download historical data as dataframe
    start_date = datetime.datetime.today() - datetime.timedelta(1825)
    end_date = datetime.datetime.today()
    data = yf.download(input_value, start=start_date, end=end_date)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': data.index, 'y': data.Close, 'type': 'line', 'name': input_value},
            ],
            'layout': {
                'title': f'Closing Prices of {input_value} Over the Last 5 Years'
            }
        }
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
