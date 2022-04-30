# # Syntax
# pandas.DataFrame.groupby(by=None[, axis=0[, level=None[, as_index=True[, sort=True[, group_keys=True[, squeeze=NoDefault.no_default[, observed=False[, dropna=True]]]]]]]])

import pandas as pd

# load the data
df = pd.read_csv('world_happiness_report_2015_2016.csv')

# split the data into 2015 subgroup and 2016 subgroup based on the column “year”
df_year = df.groupby('year')

# take a look at the first row in each subgroup
df_year_first = df_year.first()
print(df_year_first)
