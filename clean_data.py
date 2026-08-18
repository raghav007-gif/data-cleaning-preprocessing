import pandas as pd


df = pd.read_csv("data/raw_customer_data.csv")

print("Original dataset shape:", df.shape)
print("Original duplicate Customer IDs:",
      df["Customer_ID"].duplicated().sum())


df = df.drop_duplicates(subset="Customer_ID", keep="first")


df["Gender"] = (
    df["Gender"]
    .astype("string")
    .str.strip()
    .str.lower()
)

df["Gender"] = df["Gender"].replace({
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
})



df["City"] = (
    df["City"]
    .astype("string")
    .str.strip()
    .str.title()
)


df["Income"] = (
    df["Income"]
    .astype("string")
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Income"] = pd.to_numeric(
    df["Income"],
    errors="coerce"
)


df["Purchase_Amount"] = pd.to_numeric(
    df["Purchase_Amount"],
    errors="coerce"
)


df["Purchase_Date"] = (
    df["Purchase_Date"]
    .astype("string")
    .str.replace("/", "-", regex=False)
    .str.strip()
)

df["Purchase_Date"] = df["Purchase_Date"].apply(
    lambda x: pd.to_datetime(x, format="%Y-%m-%d", errors="coerce")
    if str(x).startswith("2026-")
    else pd.to_datetime(x, format="%d-%m-%Y", errors="coerce")
)


numeric_columns = [
    "Age",
    "Income",
    "Purchase_Amount"
]

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )



categorical_columns = [
    "Gender",
    "City",
    "Category"
]

for column in categorical_columns:
    if df[column].isna().any():
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )



df["Purchase_Date"] = df["Purchase_Date"].dt.strftime(
    "%Y-%m-%d"
)



print("\nCleaned dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate Customer IDs after cleaning:")
print(df["Customer_ID"].duplicated().sum())


df.to_csv(
    "data/cleaned_customer_data.csv",
    index=False
)

print("\nCleaning completed successfully!")
print("Cleaned dataset saved to:")
print("data/cleaned_customer_data.csv")
