def create_features(dataset):
    df = dataset.copy(deep=True)
    
    
    df["nps_category"] = df["nps_score"].apply(
        lambda x: "Promoter" if x >= 9 else
                  "Passive" if x >= 7 else
                  "Detractor"
    )

    

    return df