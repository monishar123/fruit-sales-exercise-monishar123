import pandas as pd

# Create the DataFrame
data = {'Apples': [35, 41], 'Bananas': [21, 34]}
index = ['2017 Sales', '2018 Sales']
fruit_sales = pd.DataFrame(data, index=index)

# Write the DataFrame to a CSV file
fruit_sales.to_csv('fruit.csv')

