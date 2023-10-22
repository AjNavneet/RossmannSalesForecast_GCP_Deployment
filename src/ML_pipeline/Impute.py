import pandas as pd
import numpy as np

def impute(df, col, method, value=0):
    """
    Impute missing values in a DataFrame column using various imputation methods.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the column with missing values.
        col (str): The name of the column to impute.
        method (str): The imputation method to use. Supported methods:
            - 'mean': Impute missing values with the mean of the column.
            - 'median': Impute missing values with the median of the column.
            - 'mode': Impute missing values with the mode of the column.
            - 'value': Impute missing values with a specified custom value.
        value (optional): The custom value to use for imputation when 'method' is set to 'value'.

    Returns:
        pd.DataFrame: The DataFrame with missing values in the specified column imputed based on the chosen method.

    Example:
        imputed_df = impute(df, 'Age', method='mean')
    """
    if method == 'mean':
        mean_val = df[col].mean()
        df[col] = df[col].fillna(mean_val)
    elif method == 'median':
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
    elif method == 'mode':
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
    elif method == 'value':
        df[col] = df[col].fillna(value)
    else:
        raise ValueError("Only these options for method are allowed: ['mean', 'median', 'mode', 'value']")
    
    return df
