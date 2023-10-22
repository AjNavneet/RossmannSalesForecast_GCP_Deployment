import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import math
import joblib

def train_model(x_train, x_test, y_train, y_test, model_name, path):
    """
    Train a regression model and save it as a pickle file.

    Parameters:
        x_train (pd.DataFrame or np.ndarray): The training features.
        x_test (pd.DataFrame or np.ndarray): The testing features.
        y_train (pd.Series or np.ndarray): The training target values.
        y_test (pd.Series or np.ndarray): The testing target values.
        model_name (str): The name of the model to train. Supported model names:
            - 'linear_reg': Linear Regression
            - 'SGD_reg': Stochastic Gradient Descent Regressor
            - 'RF_reg': Random Forest Regressor
            - 'dtree_reg': Decision Tree Regressor
        path (str): The path to save the trained model as a pickle file.

    Returns:
        np.ndarray: Predicted target values on the testing set.

    Example:
        predictions = train_model(X_train, X_test, y_train, y_test, 'linear_reg', 'model.pkl')
    """
    model_dict = {
        'linear_reg': LinearRegression,
        'SGD_reg': SGDRegressor,
        'RF_reg': RandomForestRegressor,
        'dtree_reg': DecisionTreeRegressor,
    }
    if model_name not in list(model_dict.keys()):
        raise ValueError(
            f"Only these options for model_name are allowed: {list(model_dict.keys())}")
    model = model_dict[model_name]()
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    # Save the model as a pickle file
    joblib.dump(model, path)
    print('Model saved as pkl file in ' + str(path))
    return pred
