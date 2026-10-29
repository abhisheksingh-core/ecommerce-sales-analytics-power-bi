# ecommerce_dashboard_power_bi

End-to-end E-Commerce Sales Analytics project using Python, Pandas, MySQL, SQL and Power BI with interactive dashboard and DAX KPIs.
<img width="1642" height="917" alt="image" src="https://github.com/user-attachments/assets/f5509aad-85f7-4dc7-87eb-c190acf7784f" />
# 🛒 E-Commerce Sales Analytics Dashboard

An end-to-end data analytics project that transforms raw e-commerce data into actionable business insights using Python, Pandas, MySQL, SQL and Power BI.

## 📊 Project Overview

This project analyzes e-commerce sales data to understand:

- Sales performance
- Profitability
- Monthly sales trends
- Product performance
- Category performance
- City-wise sales
- Payment method distribution
- Order status
- Average Order Value
- Profit Margin

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- MySQL
- SQL
- Power BI
- DAX
- Excel

## 🔄 Project Workflow

Raw Excel Data
        ↓
Python / Pandas
        ↓
Data Cleaning & Transformation
        ↓
MySQL
        ↓
SQL Analysis
        ↓
Power BI
        ↓
Interactive Dashboard

## 🧹 Data Cleaning

The raw dataset contained 524 records.

Cleaning steps included:

- Removed duplicate records
- Handled missing values
- Standardized text fields
- Validated email records
- Converted date columns
- Converted numeric columns
- Removed invalid quantity values
- Created Sales, Net Amount and Profit columns
- Created Month, Year and Weekday fields

After cleaning, 380 valid records remained.

## 📈 Power BI Dashboard

The dashboard includes:

### KPI Metrics

- Total Orders
- Total Sales
- Total Profit
- Average Order Value
- Profit Margin

### Visualizations

- Monthly Sales Trend
- Sales by Category
- Sales by City
- Sales by Product
- Sales by Payment Mode
- Order Status Analysis

### Filters

- Year
- Month
- City
- Category
- Payment Mode
- Order Status

## 🧮 DAX Measures

```DAX
Total Sales =
SUM(ecommerce_cleaned[Sales])

Total Profit =
SUM(ecommerce_cleaned[Profit])

Total Orders =
DISTINCTCOUNT(ecommerce_cleaned[Order_ID])

Average Order Value =
DIVIDE([Total Sales], [Total Orders])

Profit Margin =
DIVIDE([Total Profit], [Total Sales], 0)
