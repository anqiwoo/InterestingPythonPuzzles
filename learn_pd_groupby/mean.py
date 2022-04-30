import pandas as pd

# load the data
df = pd.read_csv('world_happiness_report_2015_2016.csv')

# split the data based on year, region
df_year_region = df.groupby(['year', 'Region'])[['Country', 'Happiness Rank']]

# use the mean() function to get the average Happiness Rank in each region and year
df_avg = df_year_region.mean()
print(df_avg)
