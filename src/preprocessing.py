import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled
