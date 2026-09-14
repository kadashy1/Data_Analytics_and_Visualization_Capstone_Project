import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\survey_data_updated.csv')
df_1 = df[['ResponseId', 'Age']].copy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_1 = df_1.dropna(subset=['Age'])
df_1 = df_1[(df_1['Age'] != '')]
#preview
df_gb = df_1.groupby(['Age'])['ResponseId'].nunique().reset_index(name='Respondents')
plt.figure(figsize=(10, 10))
plt.pie(df_gb['Respondents'], autopct='%1.1f%%')
plt.legend(df_gb['Age'], title='Age Group', loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Respondents by Age')
plt.show()
#save the dataset
df_1.to_csv(r'C:\Study\Data Analytics and Visualization Capstone Project\Data\Cleaned\panel_9.csv', index=False)
