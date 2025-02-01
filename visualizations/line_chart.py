import plotly.express as px

def create_line_chart(data, selected_state):
    """
    Create a line chart of population over years for a specific state.
    
    Args:
        data (pandas.DataFrame): Population dataset
        selected_state (str): State to visualize
    
    Returns:
        plotly.graph_objs._figure.Figure: Line chart figure
    """
    dff = data[data['state'] == selected_state].sort_values('year')
    fig = px.line(
        dff,
        x='year',
        y='population',
        title=f"Population Over Years: {selected_state}",
        labels={'year': 'Year', 'population': 'Population'}
    )
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    return fig
