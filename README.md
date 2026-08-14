# Data Cleaning and Preprocessing

## Internship Task 01

This project focuses on cleaning and preprocessing a customer dataset using Python and Pandas.

## Objective

The objective of this task is to identify and fix common data-quality problems such as:

- Missing values
- Duplicate records
- Inconsistent categorical values
- Inconsistent income formatting
- Inconsistent date formats

## Dataset

The dataset contains customer information including:

- Customer ID
- Customer Name
- Age
- Gender
- City
- Income
- Purchase Amount
- Purchase Date

## Data Cleaning Steps

The following preprocessing steps were performed:

1. Loaded the raw CSV dataset using Pandas.
2. Removed duplicate customer records.
3. Standardized Gender values such as `M`, `male`, `F`, and `female`.
4. Standardized city names.
5. Removed commas from income values and converted them to numeric format.
6. Converted purchase amounts to numeric values.
7. Standardized purchase dates.
8. Handled missing numerical values using the median.
9. Handled missing categorical values using the mode.
10. Saved the cleaned dataset as `cleaned_customer_data.csv`.

## Project Structure

```text
data-cleaning-preprocessing/
│
├── data/
│   ├── raw_customer_data.csv
│   └── cleaned_customer_data.csv
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── clean_data.py
├── README.md
├── .gitignore
└── .gitattributes
