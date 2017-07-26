import pandas as pd
import numpy as np


# check if record is NaN
def is_nan(x):
    return x is np.nan or x != x

ml_groups = pd.read_csv('../data/webfin.csv')
# convert columns to strings
ml_groups['Name'] = ml_groups['Name'].astype(str)
ml_groups['Phone'] = ml_groups['Phone'].astype(str)
ml_groups['Facebook'] = ml_groups['Facebook'].astype(str)

# read all students data
ml_students = pd.read_csv('../data/web.csv')

# fill the name, facebook, phone records
for index, row in ml_groups.iterrows():
    if not is_nan(row['Email']):
        print row['Email']
        fetched_row = ml_students[ml_students['Email'] == row['Email'].strip()]
        # print fetched_row ['Email'].values[0], fetched_row['Name'].values[0]
        ml_groups.set_value(index, 'Name', fetched_row['Name'].values[0])
        ml_groups.set_value(index, 'Facebook', fetched_row['Facebook'].values[0])
        ml_groups.set_value(index, 'Phone', fetched_row['Phone'].values[0])

# save filled dataframe
ml_groups.to_csv('../data/webfinal.csv')