import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['PlatformHaveWorkedWith']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_1['PlatformHaveWorkedWith'] = (df_1['PlatformHaveWorkedWith'].str.split(';'))
df_1 = df_1.explode('PlatformHaveWorkedWith')
df_1 = df_1.dropna(subset=['PlatformHaveWorkedWith'])
df_1 = df_1[(df_1['PlatformHaveWorkedWith'] != '')]
#print(df_1.head())
df_1['PlatformHaveWorkedWith'] = df_1['PlatformHaveWorkedWith'].str.strip()
#print(sorted(df_1['PlatformHaveWorkedWith'].unique()))
#print(df_1['PlatformHaveWorkedWith'].value_counts().sort_index())
#print(df_1['PlatformHaveWorkedWith'].str.lower().value_counts())
text = " ".join(df_1['PlatformHaveWorkedWith'])
wordcloud = WordCloud(width=1000, height=500, background_color="white").generate(text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_3.csv', index=False)
