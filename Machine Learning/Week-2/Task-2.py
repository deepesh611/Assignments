import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.metrics import pairwise_distances

df_iris = pd.read_csv("C:/Users/devan/Downloads/Iris.csv")

missing_columns = df_iris.columns[df_iris.isnull().any()]
if 'Id' in missing_columns:
    
    missing_columns = missing_columns.drop('Id')
print("Columns with missing values:", missing_columns)

def custom_knn_imputer(df, k=3):
    df_filled = df.copy()

    for col in df_filled.columns:
        if col == 'Id': 
            continue

        missing_indices = df_filled[df_filled[col].isnull()].index

        for idx in missing_indices:
            distances = pairwise_distances(df_filled.drop(columns=[col, 'Id']),
                                           df_filled.drop(columns=[col, 'Id']).iloc[[idx]],
                                           metric='nan_euclidean').flatten()
            nearest_indices = np.argsort(distances)[:k + 1][1:] 

            knn_values = df_filled.loc[nearest_indices, col].dropna()
            if not knn_values.empty:
                df_filled.at[idx, col] = knn_values.mean()

    return df_filled

columns_to_drop=['Id','Species']

df_custom_imputed = custom_knn_imputer(df_iris)
print("\nCustom KNN Imputed DataFrame:\n", df_custom_imputed.head())

knn_imputer = KNNImputer(n_neighbors=3, weights="uniform", metric='nan_euclidean')
df_inbuilt_imputed = pd.DataFrame(knn_imputer.fit_transform(df_iris.drop(columns=columns_to_drop)),
                                  columns=df_iris.columns.drop(columns_to_drop))
df_inbuilt_imputed.insert(0, 'Id', df_iris['Id'])
df_inbuilt_imputed.insert(5, 'Species', df_iris['Species'])  
print("\nInbuilt KNN Imputed DataFrame:\n", df_inbuilt_imputed.head())