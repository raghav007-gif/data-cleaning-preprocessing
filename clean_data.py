import pandas as pd

# 1. Load the raw dataset
df = pd.read_csv("data/raw_customer_data.csv")

print("Original dataset shape:", df.shape)

# 2. Remove duplicate records
df = df.drop_duplicates(subset="Customer_ID", keep="first")

# 3. Clean Gender values
df["Gender"] = df["Gender"].astype(str).str.strip().str.lower()
df["Gender"] = df["Gender"].replace({
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
})

# 4. Clean City values
df["City"] = df["City"].astype(str).str.strip().str.title()

# 5. Clean Income values
df["Income"] = (
    df["Income"]
    .astype(str)
    .str.replace(",", "", regex=False)
)
df["Income"] = pd.to_numeric(df["Income"], errors="coerce")

# 6. Clean Purchase Amount
df["Purchase_Amount"] = pd.to_numeric(
    df["Purchase_Amount"], errors="coerce"
)

# 7. Clean Purchase Date
df["Purchase_Date"] = pd.to_datetime(
    df["Purchase_Date"],
    dayfirst=True,
    format="mixed",
    errors="coerce"
)

# 8. Handle missing numeric values using the median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Income"] = df["Income"].fillna(df["Income"].median())
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(
    df["Purchase_Amount"].median()
)

# 9. Handle missing categorical values
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["City"] = df["City"].fillna(df["City"].mode()[0])

# 10. Save the cleaned dataset
df.to_csv("data/cleaned_customer_data.csv", index=False)

print("Cleaning completed successfully!")
print("Cleaned dataset shape:", df.shape)
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())