
import pandas as pd

# create a sample DataFrame with a date and a profit each day, and a list of categories for each day


list_b= ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']

df = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', end='2022-01-30'),
    'daily_profit': [10, 20, -5, 15, 25, -10, 5, 10, -15, 20, 30, -5, -10, 15, 20, 25, -5, -15, 10, 20, 30, -10, 5, 15, 25, -5, -15, 10, 20, 30],
    'category':list_b})

# group the DataFrame by the category list and sum up the daily profit for each category
#grouped_profit = df.groupby('category')['daily_profit'].sum()
list_a=[['1','2','3'],['a','b','c']]
#df = pd.DataFrame(list_a)
df.set_index('date')
print(df)
monthly_profit = df.daily_profit.resample('M').sum()
print(monthly_profit)
# print the grouped profit
#print(grouped_profit)
# ```
#
# In this code, we create a sample DataFrame with a date column, a daily profit column, and a category column. We then use the `groupby()` function to group the DataFrame by the category list, which is the unique values in the category column. We select the daily profit column and use the `sum()` function to calculate the total profit for each category.
#
# The resulting `grouped_profit` object is a Pandas Series with the category list as the index and the total profit for each category as the values. You can print this object using the `print()` function. print the resulting monthly profit DataFrame using the `print()` function. The resulting DataFrame will have a date index with the last day of each month, and a single column with the total profit for each month.