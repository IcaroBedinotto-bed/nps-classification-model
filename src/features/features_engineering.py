def create_features(dataset):
    df = dataset.copy(deep=True)
    
    
    #df["nps_category"] = df["nps_score"].apply( #Classificação dos clientes seguindo a metodologia NPS
        #lambda x: "Promoter" if x >= 9 else
                  #"Passive" if x >= 7 else
                  #"Detractor"
    #)

    df["nps_category"] = df["nps_score"].apply( #Verifica se o cliente é detrador seguindo a metdologia NPS
        lambda x: "Detractor" if x < 7 else
                  "Not Detractor"
    )

    return df