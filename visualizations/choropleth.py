import plotly.express as px

def create_choropleth_map(data, selected_year):
    """
    Create a choropleth map of state populations for a given year.
    
    Args:
        data (pandas.DataFrame): Population dataset
        selected_year (int): Year to visualize
    
    Returns:
        plotly.graph_objs._figure.Figure: Choropleth map figure
    """
    dff = data[data['year'] == selected_year]
    fig = px.choropleth(
        dff,
        locations='state',
        locationmode="USA-states",
        color='population',
        scope="usa",
        color_continuous_scale="Viridis",
        hover_name='state',
        labels={'population': 'Population'},
        range_color=(dff['population'].min(), dff['population'].max())
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        geo=dict(bgcolor='rgba(0,0,0,0)')
    )
    return fig
