import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.metrics import pairwise_distances

X = [
    [70.1, 154.9, 29.215, 2],
    [64.9, 157.8, np.nan, 2],
    [np.nan, 164.7, 24.73633318, 1],
    [67.5, 169.9, 23.38390377, 1],
    [68.4, 154.9, 28.5071149, np.nan],
    [77.7, 173.8, 25.72299152, 2]
]

columns = ['weight', 'height', 'BMI', 'overweight']
df = pd.DataFrame(X, columns=columns)

# Identifying columns with missing values
missing_columns = df.columns[df.isnull().any()]
print("Columns with missing values:", missing_columns)


# creating custom KNN imputer function
def custom_knn_imputer(df, k=2):
    df_filled = df.copy()

    for col in df_filled.columns:
        missing_indices = df_filled[df_filled[col].isnull()].index

        for idx in missing_indices:

            # drop----> removing all the missing values from the column and then calculating the distance
            # iloc -->  is used to get the row at the given index
            # nan_euclidean is used to calculate the distance between the two points
            # using euclidean distance
            distances = pairwise_distances(df_filled.drop(columns=[col]), df_filled.drop(columns=[col]).iloc[[idx]],
                                           metric='nan_euclidean').flatten()
            # sorting the indices according to the distances from the point we are considering
            nearest_indices = np.argsort(distances)[:k + 1][1:]  # Skip the first one (distance to itself)

            knn_values = df_filled.loc[nearest_indices, col].dropna()
            if not knn_values.empty:
                df_filled.at[idx, col] = knn_values.mean()

    return df_filled


# Applying custom KNN imputer
df_custom_imputed = custom_knn_imputer(df)
print("\nCustom KNN Imputed DataFrame:\n", df_custom_imputed)

#Using inbuilt KNNImputer function
knn_imputer = KNNImputer(n_neighbors=2, weights="uniform", metric='nan_euclidean')
df_inbuilt_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=columns)
print("\nInbuilt KNN Imputed DataFrame:\n", df_inbuilt_imputed)

#Comparing the outcomes
comparison = df_custom_imputed.equals(df_inbuilt_imputed)
print("\nAre both the imputed DataFrames equal? ->", comparison)