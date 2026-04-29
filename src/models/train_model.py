from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from src.models.model_factory import get_model

def train_model(X, y, model_name="logistic"):

    X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size = 0.3, random_state=42
    )

    if model_name=="logistic": #Caso opte trabalhar com regressão logística precisamos normalizar os dados
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    model = get_model(model_name)
    model.fit(X_train, y_train)

    return model, X_test, y_test

