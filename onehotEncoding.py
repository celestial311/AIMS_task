import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def one_hot_encode(df1, column_name):
    df=df1.copy()
    unique_categories = df[column_name].unique()
    for category in unique_categories:
        df[category] = (df[column_name] == category).astype(int)
    
    return df

