import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Orders:", df["Order_ID"].nunique())
print("Units Sold:", df["Quantity"].sum())
print("Profit Margin %:", round(df["Profit"].sum() / df["Sales"].sum() * 100, 2))

category = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
print("\nCategory performance:\n", category)

region = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
print("\nRegion performance:\n", region)

monthly = df.groupby(df["Order_Date"].dt.to_period("M"))[["Sales", "Profit"]].sum()
monthly.plot(kind="line", marker="o", title="Monthly Sales and Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()
