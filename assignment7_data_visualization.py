"""Assignment 7: Data visualization using Matplotlib and Seaborn."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_csv("sales_data.csv")
print(df.head())

month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly = df.groupby("Month")[["Sales", "Profit"]].sum().reindex(month_order)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Line plot - monthly sales trend
axes[0, 0].plot(monthly.index, monthly["Sales"], marker="o", color="blue")
axes[0, 0].set_title("Line Plot: Monthly Sales")
axes[0, 0].set_xlabel("Month"); axes[0, 0].set_ylabel("Sales")

# 2. Bar plot - total sales per product (Seaborn)
sns.barplot(data=df, x="Product", y="Sales", estimator="sum", errorbar=None, ax=axes[0, 1])
axes[0, 1].set_title("Bar Plot: Total Sales by Product")

# 3. Scatter plot - advertising vs sales
sns.scatterplot(data=df, x="Advertising", y="Sales", hue="Product", ax=axes[1, 0])
axes[1, 0].set_title("Scatter Plot: Advertising vs Sales")

# 4. Heatmap - correlation matrix
sns.heatmap(df[["Sales", "Profit", "Advertising"]].corr(), annot=True, cmap="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title("Heatmap: Correlation")

plt.tight_layout()
plt.savefig("visualization_output.png", dpi=150)
plt.show()
