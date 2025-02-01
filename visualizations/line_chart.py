import plotly.express as px

def create_line_chart(data, selected_state):
    """
    Create a line chart showing population trend for a selected state.
    
    Args:
        data (pd.DataFrame): Population data
        selected_state (str): State to visualize
    
    Returns:
        plotly.graph_objs._figure.Figure: Line chart figure
    """
    # Ensure selected_state is a string and not a Streamlit DeltaGenerator
    if not isinstance(selected_state, str):
        raise ValueError(f"Invalid state selection: {selected_state}")
    
    # Filter data for the selected state
    dff = data[data['state'] == selected_state].sort_values('year')
    
    # Create line chart
    fig = px.line(
        dff, 
        x='year', 
        y='population',
        title=f'Population Trend for {selected_state}',
        labels={'population': 'Population', 'year': 'Year'}
    )
    
    # Customize layout
    fig.update_layout(
        title_x=0.5,
        xaxis_title='Year',
        yaxis_title='Population',
        height=400
    )
    
    # Add markers to data points
    fig.update_traces(mode='lines+markers')
    
    return fig
