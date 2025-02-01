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
st.plotly_chart(choropleth_fig, use_container_width=True)

# State Selection
st.header("Population Trend")
st.write("Click on a state in the map above to see its population trend")

# Placeholder for line chart
line_chart_placeholder = st.empty()

# Add interactivity
if st.session_state.get('last_clicked_state'):
    clicked_state = st.session_state.last_clicked_state
    line_fig = create_line_chart(df, clicked_state)
    line_chart_placeholder.plotly_chart(line_fig, use_container_width=True)

# Requirements file for Streamlit Cloud
with open('requirements.txt', 'w') as f:
    f.write('''
dash==2.14.1
plotly==5.18.0
pandas==2.2.0
streamlit==1.33.0
''')
