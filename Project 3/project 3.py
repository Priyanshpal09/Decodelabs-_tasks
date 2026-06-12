import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("project 3/project 3 dataset.xlsx")

# -----------------------------
# 1. Top Products by Revenue
# -----------------------------
product_revenue = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8,5))
product_revenue.plot(kind='bar')
plt.title("Top Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# -----------------------------
# 2. Referral Source Distribution
# -----------------------------
referral_counts = df["ReferralSource"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    referral_counts,
    labels=referral_counts.index,
    autopct='%1.1f%%'
)
plt.title("Orders by Referral Source")
plt.show()

# -----------------------------
# 3. Payment Method Usage
# -----------------------------
payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(8,5))
payment_counts.plot(kind='bar')
plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()
