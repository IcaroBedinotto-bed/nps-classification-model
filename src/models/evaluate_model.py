from sklearn.metrics import classification_report, accuracy_score

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("Acurácia", accuracy_score(y_test, y_pred))
    report = classification_report(y_test, y_pred, output_dict=True)

    print(f"   Precision: {report['Detractor']['precision']:.2f}")
    print(f"   Recall:    {report['Detractor']['recall']:.2f}")
    print(f"   F1-score:  {report['Detractor']['f1-score']:.2f}\n")