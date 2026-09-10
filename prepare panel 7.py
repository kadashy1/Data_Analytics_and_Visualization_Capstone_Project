import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['PlatformWantToWorkWith', 'ResponseId']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_1['PlatformWantToWorkWith'] = (df_1['PlatformWantToWorkWith'].str.split(';'))
df_1 = df_1.explode('PlatformWantToWorkWith')
df_1 = df_1.dropna(subset=['PlatformWantToWorkWith'])
df_1 = df_1[(df_1['PlatformWantToWorkWith'] != '')]
df_1['PlatformWantToWorkWith'] = df_1['PlatformWantToWorkWith'].str.strip()
count = df_1.groupby('PlatformWantToWorkWith')['ResponseId'].nunique().sort_values(ascending=False)
top_10_df = (count.head(10).reset_index(name='Respondents'))
print(top_10_df)
print(top_10_df.dtypes)
fig = px.treemap(top_10_df, path=['PlatformWantToWorkWith'], values='Respondents', title='Top 10 Desired Platforms')
fig.show()
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_7.csv', index=False)
