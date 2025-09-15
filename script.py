import pandas as pd 
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer

def fill_missing_values(df):
    df.loc[:, 'serumalbumin'] = df['serumalbumin'].fillna(3.5)
    df.loc[:, 'lungefunksjon'] = df['lungefunksjon'].fillna(333.3)
    df.loc[:, 'kreatinin'] = df['kreatinin'].fillna(1.01)
    df.loc[:, 'hvite_blodlegemer'] = df['hvite_blodlegemer'].fillna(9)
    df.loc[:, 'blodurea_nitrogen'] = df['blodurea_nitrogen'].fillna(6.51)
    df.loc[:, 'urinmengde'] = df['urinmengde'].fillna(2502)

    #fjerner kolonner som ikke er med i modellen
    df = df.drop('bilirubin', axis=1)
    df = df.drop(["dødsfall", "sykehusdød"], axis=1)
    df = df.drop("glukose", axis=1)
    df = df.drop(["dnr_status", "dnr_dag"], axis=1)
    df = df.drop(["pasient_id", "sykdomskategori_id"], axis=1)
    
    #fjerner rader med negativ alder
    df = df[df['alder'] >= 0]

    df['adl'] = round(df['adl_pasient'].combine_first(df['adl_stedfortreder']), 2)
    df['adl_endring'] = (df['adl_pasient'] - df['adl_stedfortreder']) 

    # KNN Imputer
    def process_dataset(df, imputer):
    # Sjekker om ADL-variabler må opprettes, og beregner deretter 'adl' og 'adl_endring'
        if "adl" not in df.columns:
            df["adl"] = round(df["adl_pasient"].combine_first(df["adl_stedfortreder"]), 2)
            df["adl_endring"] = df["adl_stedfortreder"] - df["adl_pasient"]
    
        df[["adl", "adl_endring"]] = imputer.transform(df[["adl", "adl_endring"]])
    
        # Fjerner unødvendige kolonner og runder av resultatene
        df.drop(columns=["adl_stedfortreder", "adl_pasient"], inplace=True)
        df[["adl", "adl_endring"]] = df[["adl", "adl_endring"]].round(2)
    
        # Justerer 'adl_endring' for tilfeller der 'adl' er 0
        df.loc[(df["adl"] == 0) & (df["adl_endring"] != 0), "adl_endring"] = 0
        return df

    df["adl"] = round(df["adl_pasient"].combine_first(df["adl_stedfortreder"]), 2)
    df["adl_endring"] = df["adl_stedfortreder"] - df["adl_pasient"]

    knn_model = KNNImputer(n_neighbors=2)
    knn_model.fit(df[["adl", "adl_endring"]])
    
    df = process_dataset(df, knn_model)
   
    #mode
    mode_value = df["utdanning"].mode()[0]
    df["utdanning"] = df["utdanning"].fillna(mode_value)
    

    df["etnisitet"] = df["etnisitet"].fillna("other")
    df["etnisitet"] = df["etnisitet"].replace({"black": "other", "hispanic": "other", "asian": "other", "other": "other"})



    
    #dummy for inntekt
    df['inntekt_mangler'] = df['inntekt'].isnull().astype(int)
    df = pd.get_dummies(df, columns=['inntekt'], prefix='inntekt', drop_first=True)


    #mean verdi
    imputer = SimpleImputer(strategy='mean')
    df[['blod_ph', "lege_overlevelsesestimat_2mnd", "lege_overlevelsesestimat_6mnd"]] = imputer.fit_transform(df[['blod_ph', "lege_overlevelsesestimat_2mnd", "lege_overlevelsesestimat_6mnd"]])
    df = pd.get_dummies(df, columns=["kjønn" ,"sykdom_underkategori", "sykdomskategori", "kreft", "etnisitet" ], drop_first=True, dtype=int) 

   
    return df

    

