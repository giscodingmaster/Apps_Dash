import pandas as pd

def load_population_data():
    """
    Load historical state population data from GitHub.
    
    Returns:
        pandas.DataFrame: A DataFrame containing state population data
    """
    df = pd.read_csv(
        "https://raw.githubusercontent.com/JoshData/historical-state-population-csv/refs/heads/primary/historical_state_population_by_year.csv", 
        names=["state", "year", "population"]
    )
    return df

def get_unique_years(df):
    """
    Get sorted unique years from the population dataset.
    
    Args:
        df (pandas.DataFrame): Population dataset
    
    Returns:
        list: Sorted list of unique years
    """
    return sorted(df['year'].unique())
