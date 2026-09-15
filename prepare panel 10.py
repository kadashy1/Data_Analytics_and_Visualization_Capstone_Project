import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['ResponseId', 'Country']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#print(df_1['Country'].value_counts())
#print(df_1.isna().sum().sort_values(ascending=False))
df_gb = df_1.groupby(['Country'])['ResponseId'].nunique().reset_index(name='Respondents')
print(df_gb.sort_values('Respondents', ascending=False))
#save the dataset
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_10.csv', index=False)
