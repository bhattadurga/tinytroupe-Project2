import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, accuracy_score
import numpy as np

def preprocess_data(file_content: bytes):
    # Convert the bytes content to DataFrame
    data = pd.read_csv(pd.compat.StringIO(file_content.decode('utf-8')))
    
    # Handle missing values by filling with mean
    data = data.fillna(data.mean())
    
    # Split data into features and target
    X = data.drop('target', axis=1)
    y = data['target']
    
    return X, y

def train_model(X, y, model_type="auto"):
    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Model selection (auto or specific)
    if model_type == "auto":
        model = LinearRegression()  # For simplicity, using Linear Regression by default
    elif model_type == "regression":
        model = LinearRegression()
    elif model_type == "classification":
        model = LogisticRegression()
    
    model.fit(X_train, y_train)
    
    # Predictions and evaluation
    y_pred = model.predict(X_test)
    
    # Calculate R² for regression or accuracy for classification
    if model_type == "regression":
        metrics = {
            "R²": model.score(X_test, y_test),
            "MSE": mean_squared_error(y_test, y_pred)
        }
    else:
        metrics = {
            "Accuracy": accuracy_score(y_test, y_pred)
        }

    return model, metrics
