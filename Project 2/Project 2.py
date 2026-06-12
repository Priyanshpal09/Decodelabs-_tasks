import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Project 2/data.xlsx")

# ----------------------------
# Dataset Overview
# ----------------------------
print("Dataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ----------------------------
# Basic Statistics
# ----------------------------
print("\nDescriptive Statistics:")
print(df.describe())

# ----------------------------
# Mean, Median, Count
# ----------------------------
numeric_cols = df.select_dtypes(include=['number'])

print("\nMean:")
print(numeric_cols.mean())

print("\nMedian:")
print(numeric_cols.median())

print("\nCount:")
print(numeric_cols.count())

# ----------------------------
# Product Analysis
# ----------------------------
if 'Product' in df.columns:
    top_products = df['Product'].value_counts()

    print("\nTop Products:")
    print(top_products)

    top_products.plot(kind='bar')
    plt.title("Top Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Count")
    plt.show()

# ----------------------------
# Order Status Analysis
# ----------------------------
if 'OrderStatus' in df.columns:
    status_count = df['OrderStatus'].value_counts()

    print("\nOrder Status Distribution:")
    print(status_count)

    status_count.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Order Status Distribution")
    plt.ylabel("")
    plt.show()

# ----------------------------
# Monthly Revenue Trend
# ----------------------------
if 'OrderDate' in df.columns and 'TotalPrice' in df.columns:

    df['OrderDate'] = pd.to_datetime(df['OrderDate'])

    monthly_sales = df.groupby(
        df['OrderDate'].dt.to_period('M')
    )['TotalPrice'].sum()

    print("\nMonthly Revenue:")
    print(monthly_sales)

    monthly_sales.plot(kind='line', marker='o')
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()

# ----------------------------
# Outlier Detection (IQR)
# ----------------------------
if 'TotalPrice' in df.columns:

    Q1 = df['TotalPrice'].quantile(0.25)
    Q3 = df['TotalPrice'].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df['TotalPrice'] < lower_bound) |
        (df['TotalPrice'] > upper_bound)
    ]

    print("\nNumber of Outliers:", len(outliers))

    plt.boxplot(df['TotalPrice'])
    plt.title("Outlier Detection - Total Price")
    plt.show()

# ----------------------------
# Histogram
# ----------------------------
if 'TotalPrice' in df.columns:

    plt.hist(df['TotalPrice'], bins=20)
    plt.title("Total Price Distribution")
    plt.xlabel("Total Price")
    plt.ylabel("Frequency")
    plt.show()

# ----------------------------
# Key Insights
# ----------------------------
print("\nAnalysis Completed Successfully!")