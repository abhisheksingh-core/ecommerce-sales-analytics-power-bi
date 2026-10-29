import pandas as pd
import numpy as np

# Load data
df = pd.read_excel('Ecommerce_Unclean_Project.xlsx')

# Initial analysis
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.columns)
print("Shape:", df.shape)


# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicates
df.drop_duplicates(inplace=True)

# Replace invalid/missing values
df.replace(
    ['N/A', 'na', 'NaN', 'nan', 'None'],
    np.nan,
    inplace=True
)

# Remove extra spaces from text columns
df = df.apply(
    lambda x: x.str.strip() if x.dtype == "object" else x
)

# Standardize text columns
df['Customer_Name'] = df['Customer_Name'].str.title()
df['City'] = df['City'].str.title()
df['State'] = df['State'].str.title()

# Keep only valid emails
df = df[df['Email'].str.contains('@', na=False)]

# Convert dates
df['Order_Date'] = pd.to_datetime(
    df['Order_Date'],
    errors='coerce'
)

df['Delivery_Date'] = pd.to_datetime(
    df['Delivery_Date'],
    errors='coerce'
)

# Convert numeric columns
cols = ['Qty', 'Unit_Price', 'Discount']

for c in cols:
    df[c] = pd.to_numeric(
        df[c],
        errors='coerce'
    )

# Keep positive quantities
df = df[df['Qty'] > 0]

# Fill missing values
df['Phone'] = df['Phone'].fillna('Unknown')

df['Discount'] = df['Discount'].fillna(0)

df['Delivery_Date'] = df['Delivery_Date'].fillna(
    df['Order_Date']
)


# -----------------------------
# CALCULATED COLUMNS
# -----------------------------

# Sales
df['Sales'] = df['Qty'] * df['Unit_Price']

# Net Amount
df['Net_Amount'] = (
    df['Sales'] -
    (df['Sales'] * df['Discount'] / 100)
)

# Profit
df['Profit'] = df['Net_Amount'] * 0.20

# Date features
df['Month'] = df['Order_Date'].dt.month_name()

df['Year'] = df['Order_Date'].dt.year

df['Weekday'] = df['Order_Date'].dt.day_name()


# -----------------------------
# FINAL CHECK
# -----------------------------

print("\nAfter Cleaning:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFinal Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())



df.to_csv('Ecommerce_Cleaned_Project.csv', index=False)