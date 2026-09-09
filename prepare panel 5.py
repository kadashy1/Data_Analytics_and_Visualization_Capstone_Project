import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['ResponseId', 'LanguageWantToWorkWith', 'DevType']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_1['LanguageWantToWorkWith'] = (df_1['LanguageWantToWorkWith'].str.split(';'))
df_1 = df_1.explode('LanguageWantToWorkWith')
df_1['DevType'] = (df_1['DevType'].str.split(';'))
df_1 = df_1.explode('DevType')
df_1 = df_1.dropna(subset=['LanguageWantToWorkWith', 'DevType'])
df_1 = df_1[(df_1['LanguageWantToWorkWith'] != '') & (df_1['DevType'] != '')]
#matplotlib preview
df_gb = df_1.groupby(['LanguageWantToWorkWith', 'DevType'])['ResponseId'].nunique().reset_index(name='Respondents')
df_pv = df_gb.pivot(index='LanguageWantToWorkWith', columns='DevType', values='Respondents').fillna(0)
top_10 = df_pv.sum(axis=1).sort_values(ascending=False).head(10).index
df_pv10 = df_pv.loc[top_10]
dev5 = df_pv10.sum(axis=0).sort_values(ascending=False).head(5).index
df_pv10 = df_pv10[dev5]
df_pv10 = df_pv10.loc[df_pv10.sum(axis=1).sort_values().index]
df_pv10.plot(kind='barh', stacked=True, figsize=(12, 8))
plt.title('Top 10 Languages desired by Developer Type')
plt.xlabel('Number of Respondents')
plt.ylabel('Language')
plt.legend(
    title='Developer Type',
    bbox_to_anchor=(1.05, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()
#save the dataset
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_5.csv', index=False)
