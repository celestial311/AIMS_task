import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def order(num_categories):
    category_order = []
    for i in range(num_categories):
        ele = input(f"Enter Category {i + 1}: ")
        category_order.append(ele)
    return category_order

def ordinal_encode(df1, column_name, category_order):
    df=df1.copy()
    category_mapping = {}
    for i in range(len(category_order)):
        category_mapping[category_order[i]] = i

    df[column_name + '_Encoded'] = df[column_name].map(category_mapping)
    return df
