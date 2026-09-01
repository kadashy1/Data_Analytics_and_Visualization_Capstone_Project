import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['ResponseId', 'LanguageHaveWorkedWith', 'DevType']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#print(df_1.shape)
#for column in df_1.columns:
#    print(column)
df_1['LanguageHaveWorkedWith'] = (df_1['LanguageHaveWorkedWith'].str.split(';'))
df_1 = df_1.explode('LanguageHaveWorkedWith')
df_1['DevType'] = (df_1['DevType'].str.split(';'))
df_1 = df_1.explode('DevType')
#remove missing values and empty strings
df_1 = df_1.dropna(subset=['LanguageHaveWorkedWith', 'DevType'])
df_1 = df_1[(df_1['LanguageHaveWorkedWith'] != '') & (df_1['DevType'] != '')]
#check resulting data
#print(df_1.shape)
#print(df_1.head(20))
#print(df_1['LanguageHaveWorkedWith'].value_counts().head(20))
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_1.csv', index=False)
