from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def get_model(model_name):

    if model_name == "logistic":
        return LogisticRegression(max_iter=2000, class_weight="balanced")

    elif model_name == "random_forest":
        return RandomForestClassifier(
            n_estimators=100,
            class_weight="balanced",
            random_state=42
        )

