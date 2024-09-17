import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Given dataset
X = [
    [70.1, 154.9, 29.215, 2],
    [64.9, 157.8, np.NaN, 2],
    [np.NaN, 164.7, 24.73633318, 1],
    [67.5, 169.9, 23.38390377, 1],
    [68.4, 154.9, 28.5071149, np.NaN],
    [77.7, 173.8, 25.72299152, 2]
]

# Step 1: Initialize missing values with the mean of the column
def initialize_missing_values(X):
    for j in range(len(X[0])):
        col_values = [X[i][j] for i in range(len(X)) if not np.isnan(X[i][j])]
        mean_value = sum(col_values) / len(col_values)
        for i in range(len(X)):
            if np.isnan(X[i][j]):
                X[i][j] = mean_value
    return X

# Step 2: Fit linear regression and predict missing values
def linear_regression_predict(X, target_index, feature_indices):
    X_train = []
    y_train = []
    
    # Prepare training data
    for i in range(len(X)):
        if not np.isnan(X[i][target_index]):
            y_train.append(X[i][target_index])
            X_train.append([X[i][j] for j in feature_indices])
    
    # Calculate weights (coefficients) for linear regression
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    
    X_transpose = np.transpose(X_train)
    X_transpose_X = np.dot(X_transpose, X_train)
    X_transpose_y = np.dot(X_transpose, y_train)
    
    # Weight vector w = (X^T * X)^-1 * X^T * y
    w = np.linalg.solve(X_transpose_X, X_transpose_y)
    
    # Predict missing values
    for i in range(len(X)):
        if np.isnan(X[i][target_index]):
            X[i][target_index] = np.dot(w, [X[i][j] for j in feature_indices])
    return X

# Step 3: Iterative Imputation
def iterative_imputation(X, iterations=10):
    X = initialize_missing_values(X)
    feature_indices = [i for i in range(len(X[0]))]
    
    for _ in range(iterations):
        for i in range(len(X[0])):
            target_index = i
            other_indices = [j for j in feature_indices if j != target_index]
            X = linear_regression_predict(X, target_index, other_indices)
    
    return X

# Perform iterative imputation
X_imputed = iterative_imputation(X)

# Print the imputed dataset
for row in X_imputed:
    print(row)

X = np.array(X)

# Create an IterativeImputer object
imputer = IterativeImputer(max_iter=10, random_state=0)

# Perform iterative imputation
X_imputed = imputer.fit_transform(X)

# Print the imputed dataset
print("imputed",X_imputed)