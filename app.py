import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import socket

from data_loader import load_population_data, get_unique_years
from visualizations.choropleth import create_choropleth_map
from visualizations.line_chart import create_line_chart

# Load data
df = load_population_data()
unique_years = get_unique_years(df)

# Initialize app
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1("US State Population Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': year} for year in unique_years],
            value=unique_years[-1],
            clearable=False
        ),
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    
    dcc.Graph(
        id='choropleth-map',
        style={'width': '70%', 'display': 'inline-block', 'height': '600px'}
    ),
    
    dcc.Graph(
        id='line-chart',
        style={'width': '90%', 'margin': '0 auto', 'display': 'block', 'height': '400px'}
    ),
])

# Callbacks
@app.callback(
    Output('choropleth-map', 'figure'),
    Input('year-dropdown', 'value')
)
def update_choropleth(selected_year):
    return create_choropleth_map(df, selected_year)

@app.callback(
    Output('line-chart', 'figure'),
    Input('choropleth-map', 'clickData'),
    Input('year-dropdown', 'value')
)
def update_line_chart(clickData, selected_year):
    if clickData is not None:
        clicked_state = clickData['points'][0]['location']
        return create_line_chart(df, clicked_state)
    else:
        return px.line(title="Click a state on the map to see its population over the years")

if __name__ == '__main__':
    # Get local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Access the app at:")
    print(f"- Local: http://127.0.0.1:8050/")
    print(f"- Network: http://{local_ip}:8050/")
    
    # Run the app on all interfaces
    app.run_server(debug=True, port=8050, host='0.0.0.0')
