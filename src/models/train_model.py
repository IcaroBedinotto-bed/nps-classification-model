from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def train_model(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state=42
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(class_weight="balanced")

    #Treinar o modelo
    model.fit(X_train, y_train)

    return model, X_test, y_test

