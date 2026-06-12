import pandas as pd

df = pd.read_excel("dataAnalyst/Dataset.xlsx")
print(df.head())

# Identify Missing Values
print("Missing Values:")
print(df.isnull().sum())

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

df["Date"] = pd.to_datetime(df["Date"])
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"])
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"])


df["Product"] = df["Product"].str.strip().str.title()
df["OrderStatus"] = df["OrderStatus"].str.strip().str.title()

df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Dataset cleaned successfully!")