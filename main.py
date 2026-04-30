from src.data.data_processing import load_data
from src.features.features_engineering import create_features
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model

def main():

    dataset = load_data()

    df = create_features(dataset)

    X = df[[
    "customer_age",
    "customer_tenure_months",
    "order_value",
    "items_quantity",
    "discount_value",
    "payment_installments",
    "delivery_time_days",
    "delivery_delay_days",
    "freight_value",
    "delivery_attempts",
    "customer_service_contacts",
    "resolution_time_days",
    "complaints_count",
    "csat_internal_score"]] #Escolhas de variáveis que acontecem antes da pesquisa de NPS, permitindo agir de maneira proativa

    y = df["nps_category"] 

    model, X_test, y_test = train_model(X, y, model_name = "logistic") #Dado que existe um desbalanceamento dos dados para detratores, faz sentido optar pelo Random Forest

    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()


