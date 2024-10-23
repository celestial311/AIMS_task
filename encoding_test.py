import onehotEncoding as ohe
import ordinalEncoding as oe

file_path = input("Enter file path: ")
df = oe.load_data(file_path)

cat = int(input("Number of unique categories: "))
category_order = oe.order(cat)
cat_name= input("Enter the column to Encode: ")
df_encoded = oe.ordinal_encode(df,cat_name , category_order)

print("Original Data:")
print(df)
print("\nOrdinal Encoded Data:")
print(df_encoded)
print(df)

file_path = input("Enter file path: ")
df = ohe.load_data(file_path)
column_name = input("Enter the column to Encoded: ")
df_encoded = ohe.one_hot_encode(df, column_name)
print("Original Data:")
print(df)  
print("\nOne-Hot Encoded Data:")
print(df_encoded)  