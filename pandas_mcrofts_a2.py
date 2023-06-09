import pandas as pd
csv_path='a2_data.csv'
df=pd.read_csv(csv_path)
print("Emily's Info:")
print(df.loc[4,'Name':'Qualify'])
print('\n')
print('Names of Participants:')
x=df[['Name']]
print(x)
print('\n')
y=df.loc[0,'Attempts'] + df.loc[1,'Attempts'] + df.loc[2,'Attempts'] + df.loc[3,'Attempts'] + df.loc[4,'Attempts']
print('Average Number of Attempts: ', y/5)
print('\n')
xlsx_path='a2_data.xlsx'
df2=pd.read_excel(xlsx_path)
print('Number of Rows: ', len(df2))
print('Number of Columns: ', len(df2.columns))
print('\n')
print('Qualifiers:')
z=df[df2['Score']>10]
print(z)
z.to_csv('a2_qualifiers.csv')
