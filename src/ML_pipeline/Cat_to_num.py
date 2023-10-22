import pandas as pd
import numpy as np
from sklearn import preprocessing

def cat_to_num(df, col, method='default', values=None):
    """
    Convert categorical data to numerical data in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        col (str): The name of the categorical column to be converted.
        method (str, optional): The method for conversion. 
            - 'default': Uses LabelEncoder for standard encoding.
            - 'custom': Applies custom encoding using a provided dictionary of values.
        values (dict, optional): A dictionary mapping categorical values to their corresponding numerical values.

    Returns:
        pd.DataFrame: The DataFrame with the categorical column converted to numerical.

    Raises:
        ValueError: If an unsupported 'method' is provided.

    Example:
        cat_to_num(df, 'Category', method='custom', values={'A': 0, 'B': 1, 'C': 2})
    """
    if method == 'default':
        # Use LabelEncoder for standard encoding
        label_encoder = preprocessing.LabelEncoder()
        df[col] = label_encoder.fit_transform(df[col])
        return df
    elif method == 'custom':
        # Apply custom encoding using the provided dictionary of values
        for key, val in values.items():
            df[col].loc[df[col] == key] = val
        return df
    else:
        raise ValueError(
            "Only these options for method are allowed: ['default', 'custom']")
