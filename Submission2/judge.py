from sklearn.metrics import mean_squared_error, accuracy_score

def evaluate_model(model):
    # Evaluate model using test data (for demonstration purposes, using random data)
    X_test = np.random.rand(10, 5)
    y_test = np.random.randint(0, 2, 10)
    
    y_pred = model.predict(X_test)
    
    # For classification or regression evaluation
    score = accuracy_score(y_test, y_pred)  # or R² for regression models
    suggestions = "Consider feature scaling or using more advanced models."
    
    return score, suggestions
