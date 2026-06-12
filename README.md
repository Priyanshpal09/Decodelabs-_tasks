# Data Analyst Project

A Python-based data cleaning and preprocessing tool for analyzing and preparing sales/order data from Excel files.

## Overview

This project reads raw sales data from an Excel file, cleans and standardizes it, handles missing values, and exports the cleaned dataset for further analysis or reporting.

## Features

- **Missing Value Handling**: Identifies and intelligently fills missing values (e.g., missing coupon codes are replaced with "No Coupon")
- **Data Type Conversion**: Automatically converts date, quantity, and price columns to appropriate data types
- **Text Cleaning**: Removes extra whitespace and applies proper title casing to text fields
- **Excel Export**: Saves the cleaned dataset to a new Excel file for easy access

## Requirements

- Python 3.x
- pandas
- openpyxl (for Excel file handling)

## Installation

1. Clone or download the project
2. Install required dependencies:
```bash
pip install pandas openpyxl
```

## Usage

1. Place your dataset file named `Dataset.xlsx` in the `dataAnalyst/` directory
2. Run the script:
```bash
python main.py
```
3. The cleaned dataset will be saved as `Cleaned_Dataset.xlsx`

## Data Processing Steps

1. **Load Data**: Reads the Excel file from `dataAnalyst/Dataset.xlsx`
2. **Missing Value Detection**: Displays all columns with missing values
3. **Missing Value Imputation**: Fills missing `CouponCode` values with "No Coupon"
4. **Data Type Conversion**: 
   - Converts `Date` column to datetime format
   - Converts `Quantity`, `UnitPrice`, and `TotalPrice` to numeric types
5. **Text Cleaning**:
   - Strips whitespace from `Product` and `OrderStatus` columns
   - Applies title case formatting
6. **Export**: Saves the cleaned data to `Cleaned_Dataset.xlsx`

## Expected Input File Format

The input `Dataset.xlsx` should contain columns such as:
- Date
- Product
- Quantity
- UnitPrice
- TotalPrice
- CouponCode
- OrderStatus

## Output

The script generates:
- Console output showing data preview and data cleaning progress
- `Cleaned_Dataset.xlsx` - The cleaned and processed dataset

## Notes

- Missing coupon codes are filled with "No Coupon" - modify this value in `main.py` as needed
- Ensure the input file path is correct before running the script
- The script preserves all rows while cleaning data
