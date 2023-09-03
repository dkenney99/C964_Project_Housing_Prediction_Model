import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'SQL CLEANED DATA.csv'  # replace with your file's path
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['legal_acrea_in_acres'], df['soldprice'], color='blue', alpha=0.5)
plt.title('Scatter Plot: Sold Price vs Legal Area in Acres')
plt.xlabel('Legal Area in Acres')
plt.ylabel('Sold Price')
plt.grid(True)
plt.show()