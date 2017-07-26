import pandas as pd

df = pd.read_csv('./data/studygroups.csv', encoding='utf-8')

# lowercase all email entries, remove trailing spaces
df['Email'] = df['Email'].map(lambda x: x if type(x) != str else x.lower().strip())

# find duplicate emails
# print(pd.concat(g for _, g in df.groupby('Email') if len(g) > 1)[['Email', 'Learning path']])

# split into different dataframes based on Learning paths
ml_df = df[df.path == 'Machine Learning']
mobile_df = df[df.path == 'Android Development']
web_df = df[df.path == 'Full Stack']

# df.drop(['Timestamp', 'Email', 'Name', 'Facebook', 'Phone', 'communication', 'experience', 'motivation'], axis=1, inplace=True)
ml_df.to_csv('./data/ml.csv')
web_df.to_csv('./data/web.csv')
mobile_df.to_csv('/data/mobile.csv')
print(ml_df.shape, mobile_df.shape, web_df.shape)