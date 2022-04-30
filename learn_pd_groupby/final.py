import pandas as pd

# load the data
df = pd.read_csv('world_happiness_report_2015_2016.csv')

# use the count() function to get the number of top 10 countries in a region each year
df_top_10 = df[df['Happiness Rank'] <= 10]
df_year_region = df_top_10.groupby(['year', 'Region'])['Country']
top_10_count = df_year_region.count()
print('The number of top 10 countries in a region each year:')
print(top_10_count)
print('-'*85)

# use the min() function to get the top ranked country in a region each year
df_year_region = df.groupby(['year', 'Region'])[['Country', 'Happiness Rank']]
top_country = df_year_region.min()
print('The top ranked country in a region each year:')
print(top_country)
print('-'*85)

# use the max() function to get least ranked country in a region each year.
df_year_region = df.groupby(['year', 'Region'])[['Country', 'Happiness Rank']]
least_country = df_year_region.max()
print('The least ranked country in a region each year:')
print(least_country)
