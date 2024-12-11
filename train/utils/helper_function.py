def map_unique_values(df, column_name):
    """
    Maps unique values in a specified column of a DataFrame to integers and updates the column.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the column to map.
        column_name (str): The name of the column to map.
    
    Returns:
        dict: A dictionary containing the mapping of unique values to integers.
    """
    # Get unique values and create a mapping
    unique_values = df[column_name].unique()
    value_mapping = {value: idx for idx, value in enumerate(unique_values)}
    
    # Replace column values with their mapped integers
    df[column_name] = df[column_name].map(value_mapping)