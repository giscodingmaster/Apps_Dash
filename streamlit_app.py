import streamlit as st
import plotly.express as px

from data_loader import load_population_data, get_unique_years
from visualizations.choropleth import create_choropleth_map
from visualizations.line_chart import create_line_chart

# Load data
@st.cache_data
def load_data():
    df = load_population_data()
    return df, get_unique_years(df)

df, unique_years = load_data()

# Page title
st.title("US State Population Dashboard")

# Sidebar for year selection
selected_year = st.sidebar.selectbox(
    "Select Year", 
    unique_years, 
    index=len(unique_years)-1
)

# Choropleth Map
st.header("Population Choropleth Map")
choropleth_fig = create_choropleth_map(df, selected_year)

# Add hover template to show more information
choropleth_fig.update_traces(
    hovertemplate='<b>%{location}</b><br>Population: %{z:,.0f}<extra></extra>'
)

# State selection
st.header("Population Trend")

# Render the map with selection
selected_state = st.plotly_chart(
    choropleth_fig, 
    on_select="rerun",
    key="population_map"
)

# Debugging: Print selected_state type and value
st.write(f"Debug - Selected State Type: {type(selected_state)}")
st.write(f"Debug - Selected State Value: {selected_state}")

# Ensure selected_state is a string
if selected_state and isinstance(selected_state, str):
    st.write(f"Selected State: {selected_state}")
    
    # Create line chart for selected state
    try:
        line_fig = create_line_chart(df, selected_state)
        st.plotly_chart(line_fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating line chart: {e}")
else:
    st.write("Click on a state in the map to see its population trend")

# Requirements file for Streamlit Cloud
with open('requirements.txt', 'w') as f:
    f.write('''
dash==2.14.1
plotly==5.18.0
pandas==2.2.0
streamlit==1.33.0
''')
