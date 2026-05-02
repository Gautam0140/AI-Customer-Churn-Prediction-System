import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(path):
    df = pd.read_csv(path)

    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    df = df.dropna()

    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    return df
