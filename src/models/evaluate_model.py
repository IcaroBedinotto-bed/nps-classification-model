from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("Acurácia", accuracy_score(y_test, y_pred))
    report = classification_report(y_test, y_pred, output_dict=True)

    for classe in ["Promoter", "Passive", "Detractor"]:
        if classe in report:
            print(f"📌 {classe}:")
            print(f"   Precision: {report[classe]['precision']:.2f}")
            print(f"   Recall:    {report[classe]['recall']:.2f}")
            print(f"   F1-score:  {report[classe]['f1-score']:.2f}\n")