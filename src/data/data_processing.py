import pandas as pd

def load_data():
    dataset = pd.read_csv("src\data\desafio_nps.csv")
    return dataset