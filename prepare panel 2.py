import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['ResponseId', 'DatabaseHaveWorkedWith', 'DevType']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_1['DatabaseHaveWorkedWith'] = (df_1['DatabaseHaveWorkedWith'].str.split(';'))
df_1 = df_1.explode('DatabaseHaveWorkedWith')
df_1['DevType'] = (df_1['DevType'].str.split(';'))
df_1 = df_1.explode('DevType')
df_1 = df_1.dropna(subset=['DatabaseHaveWorkedWith', 'DevType'])
df_1 = df_1[(df_1['DatabaseHaveWorkedWith'] != '') & (df_1['DevType'] != '')]
df_gb = df_1.groupby(['DatabaseHaveWorkedWith', 'DevType'])['ResponseId'].nunique().reset_index(name='Respondents')
#print(df_gb.head(10))
df_pv = df_gb.pivot(index='DatabaseHaveWorkedWith', columns='DevType', values='Respondents').fillna(0)
#print(df_pv.head(10))
top_10 = df_pv.sum(axis=1).sort_values(ascending=False).head(10).index
df_pv10 = df_pv.loc[top_10]
dev5 = df_pv10.sum(axis=0).sort_values(ascending=False).head(5).index
df_pv10 = df_pv10[dev5]
df_pv10 = df_pv10.loc[df_pv10.sum(axis=1).sort_values().index]
df_pv10.plot(kind='barh', stacked=True, figsize=(12, 8))
plt.title('Top 10 databases Used by Developer Type')
plt.xlabel('Number of Respondents')
plt.ylabel('database')
plt.legend(
    title='Developer Type',
    bbox_to_anchor=(1.05, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()

df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_2.csv', index=False)
