import pandas as pd
import numpy as np

def feature_importance(X_train_cols, model):
    """
    Calculate feature importance scores for a trained model.

    Parameters:
        X_train_cols (list or array-like): The names or columns of the features used during training.
        model: The trained model for which you want to calculate feature importance.

    Returns:
        pd.DataFrame: A DataFrame containing feature names and their corresponding importance values, sorted by importance in descending order.

    Example:
        importance_df = feature_importance(X_train.columns, trained_model)
    """
    feature_importance = model.feature_importances_
    feature_importance_value = [round(val, 5) for val in feature_importance]
    feature_importance_df = pd.DataFrame({"Features": X_train_cols, "Values": feature_importance_value})
    feature_importance_df.sort_values(by=["Values"], inplace=True, ascending=False)
    return feature_importance_df
