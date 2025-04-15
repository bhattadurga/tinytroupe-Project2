import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score

def train_model(file_path, model_type):
    df = pd.read_csv(file_path)
    target = df.columns[-1]
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    if model_type.lower() == "regression":
        model = LinearRegression()
    else:
        model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if model_type.lower() == "regression":
        metric = r2_score(y_test, y_pred)
    else:
        metric = accuracy_score(y_test, y_pred)

    return {
        "model_type": model_type,
        "metrics": metric,
        "model": model,
        "performance_summary": f"Model achieved score: {metric}"
    }
