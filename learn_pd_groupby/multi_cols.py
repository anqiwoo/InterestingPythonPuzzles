import pandas as pd

# load the data
df = pd.read_csv('world_happiness_report_2015_2016.csv')

# split the data based on year, region
df_year_region = df.groupby(['year', 'Region'])

# get the top-scored country records in each region and year
df_year_region_first = df_year_region.first()[['Country', 'Happiness Rank']]
print(df_year_region_first)
