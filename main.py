import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data.csv')
print(f"Before: {df.shape}")


df.drop_duplicates(inplace=True)


df['City'] = df['City'].str.strip().str.title()

df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Price'] = df['Price'].fillna(df['Price'].median())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
df['City'] = df['City'].fillna('Accra')
# Handle Date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# 5. Create new column
df['Total_Sales'] = df['Price'] * df['Quantity']
# 6. Clean again after filling
df.dropna(subset=['Product'], inplace=True)
print(f"After: {df.shape}")
print(df.head())

df.to_csv('cleaned_data.csv', index=False)


plt.figure(figsize=(8,5))
sns.barplot(x='City', y='Total_Sales', data=df, estimator=sum, ci=None)
plt.title('Total Sales by City')
plt.tight_layout()
plt.savefig('sales_by_city.png')
plt.show()
print("Done! Files created: cleaned_data.csv and sales_by_city.png")