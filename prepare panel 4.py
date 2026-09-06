import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['ResponseId', 'WebframeHaveWorkedWith', 'Age']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_1['WebframeHaveWorkedWith'] = (df_1['WebframeHaveWorkedWith'].str.split(';'))
df_1 = df_1.explode('WebframeHaveWorkedWith')
df_1 = df_1.dropna(subset=['WebframeHaveWorkedWith', 'Age'])
df_1 = df_1[(df_1['WebframeHaveWorkedWith'] != '') & (df_1['Age'] != '')]
age_ranges = {
    'Under 18 years old': (0, 17),
    '18-24 years old': (18, 24),
    '25-34 years old': (25, 34),
    '35-44 years old': (35, 44),
    '45-54 years old': (45, 54),
    '55-64 years old': (55, 64),
    '65 years or older': (65, 90),
    'Prefer not to say': (0 , 90)
}
def random_age(age_grp):
    if age_grp in age_ranges:
        low, high = age_ranges[age_grp]
        return np.random.randint(low, high + 1)
    return np.nan

df_1['AgeN'] = df_1['Age'].apply(random_age)
#mpl preview
df_gb = df_1.groupby(['WebframeHaveWorkedWith', 'AgeN'])['ResponseId'].nunique().reset_index(name='Respondents')
top_10 = df_gb.groupby('WebframeHaveWorkedWith')['Respondents'].sum().sort_values(ascending=False).head(10).index
df_b = df_gb[df_gb['WebframeHaveWorkedWith'].isin(top_10)].copy()
plt.scatter(df_b['WebframeHaveWorkedWith'], df_b['Respondents'], s=df_b['AgeN'] * 5, alpha=0.5)
plt.xticks(rotation=90)
plt.xlabel('Web frames')
plt.ylabel('Popularity')
plt.title('Web frame Popularity - size = user age')
plt.show()
#save the dataset
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_4.csv', index=False)
