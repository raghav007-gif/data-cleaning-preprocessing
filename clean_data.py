import pandas as pd

# -----------------------------------------
# 1. Load the raw dataset
# -----------------------------------------

df = pd.read_csv("data/raw_customer_data.csv")

print("Original dataset shape:", df.shape)
print("Original duplicate Customer IDs:",
      df["Customer_ID"].duplicated().sum())


# -----------------------------------------
# 2. Remove duplicate customer records
# -----------------------------------------

df = df.drop_duplicates(subset="Customer_ID", keep="first")


# -----------------------------------------
# 3. Clean Gender values
# -----------------------------------------

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


# -----------------------------------------
# 4. Clean City values
# -----------------------------------------

df["City"] = (
    df["City"]
    .astype("string")
    .str.strip()
    .str.title()
)


# -----------------------------------------
# 5. Clean Income
# -----------------------------------------

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


# -----------------------------------------
# 6. Clean Purchase Amount
# -----------------------------------------

df["Purchase_Amount"] = pd.to_numeric(
    df["Purchase_Amount"],
    errors="coerce"
)


# -----------------------------------------
# 7. Clean Purchase Date
# -----------------------------------------

# Convert slash separators to hyphens
df["Purchase_Date"] = (
    df["Purchase_Date"]
    .astype("string")
    .str.replace("/", "-", regex=False)
    .str.strip()
)

# All dates in the dataset follow YYYY-MM-DD
# after separator normalization.
df["Purchase_Date"] = pd.to_datetime(
    df["Purchase_Date"],
    format="mixed",
    errors="coerce"
)


# -----------------------------------------
# 8. Handle missing numerical values
# -----------------------------------------

numeric_columns = [
    "Age",
    "Income",
    "Purchase_Amount"
]

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )


# -----------------------------------------
# 9. Handle missing categorical values
# -----------------------------------------

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


# -----------------------------------------
# 10. Format the date consistently
# -----------------------------------------

df["Purchase_Date"] = df["Purchase_Date"].dt.strftime(
    "%Y-%m-%d"
)


# -----------------------------------------
# 11. Verification
# -----------------------------------------

print("\nCleaned dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate Customer IDs after cleaning:")
print(df["Customer_ID"].duplicated().sum())


# -----------------------------------------
# 12. Save cleaned dataset
# -----------------------------------------

df.to_csv(
    "data/cleaned_customer_data.csv",
    index=False
)

print("\nCleaning completed successfully!")
print("Cleaned dataset saved to:")
print("data/cleaned_customer_data.csv")
