import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import math

def evaluate_results(y_test, y_pred):
    """
    Evaluate the performance of a regression model by calculating various metrics.

    Parameters:
        y_test (array-like): The true target values from the test dataset.
        y_pred (array-like): The predicted target values from the regression model.

    Returns:
        dict: A dictionary containing evaluation metrics.
            - 'r2_score': The coefficient of determination (R^2).
            - 'mae': Mean Absolute Error (MAE).
            - 'rmse': Root Mean Squared Error (RMSE).

    Example:
        metrics = evaluate_results(y_true, y_predicted)
    """
    metrics = {
        'r2_score': r2_score(y_test, y_pred),
        'mae': mean_absolute_error(y_test, y_pred),
        'rmse': math.sqrt(mean_squared_error(y_test, y_pred)),
    }
    return metrics
