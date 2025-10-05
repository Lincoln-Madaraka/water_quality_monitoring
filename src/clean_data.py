import pandas as pd

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sensor data by handling missing or invalid values.

    Returns:
        pd.DataFrame: Cleaned data.
    """
   df = df.copy()
    
    # Fill missing with None (or could drop them)
    df = df.where(pd.notnull(df), None)
    
    # Ensure valid ranges
    df.loc[(df['ph'] < 0) | (df['ph'] > 14), 'ph'] = None
    df.loc[df['turbidity'] < 0, 'turbidity'] = None
    
    return df