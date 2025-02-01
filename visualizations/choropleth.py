import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

def create_choropleth_map(data, selected_year):
    """
    Create a choropleth map of state populations for a given year.
    
    Args:
        data (pandas.DataFrame): Population dataset
        selected_year (int): Year to visualize
    
    Returns:
        plotly.graph_objs._figure.Figure: Choropleth map figure
    """
    # Filter data for the selected year
    year_df = data[data['year'] == selected_year]
    
    # Create choropleth map
    fig = px.choropleth(
        year_df, 
        locations='state', 
        locationmode='USA-states', 
        color='population',
        scope='usa',
        color_continuous_scale='Viridis',
        title=f'US Population by State in {selected_year}',
        labels={'population': 'Population'}
    )
    
    # Customize hover template
    fig.update_traces(
        hovertemplate='<b>%{location}</b><br>Population: %{z:,.0f}<extra></extra>',
        marker_line_color='white',
        marker_line_width=0.5
    )
    
    # Adjust layout for better readability
    fig.update_layout(
        title_x=0.5,
        geo_scope='usa',
        height=600,
        margin={"r":0,"t":50,"l":0,"b":0}
    )
    
    return fig
