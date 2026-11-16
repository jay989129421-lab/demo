"""Assignment 6: Data preprocessing on a CSV file using pandas."""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Load data
df = pd.read_csv("students_raw.csv")
print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)
print("\nInfo:")
df.info()
print("\nStatistics:\n", df.describe())

# 2. Check missing values
print("\nMissing values:\n", df.isnull().sum())

# 3. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())        # numeric -> median
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())    # numeric -> mean
df["Branch"] = df["Branch"].fillna(df["Branch"].mode()[0])  # categorical -> mode

# 4. Remove duplicates
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# 5. Handle outliers in Marks (IQR method) - cap values to valid range
q1, q3 = df["Marks"].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
df["Marks"] = df["Marks"].clip(lower, upper)

# 6. Fix data types
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].round(2)

# 7. Encode categorical data
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df = pd.get_dummies(df, columns=["Branch"], dtype=int)

# 8. Feature scaling (Min-Max)
df["Marks_Scaled"] = MinMaxScaler().fit_transform(df[["Marks"]])

# 9. Save cleaned data
df.to_csv("students_cleaned.csv", index=False)
print("\nCleaned data:\n", df.head())
print("\nMissing values after cleaning:", df.isnull().sum().sum())
print("Cleaned file saved as students_cleaned.csv")
