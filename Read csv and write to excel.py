import pandas as pd

df = pd.read_csv('Report_Dividend_as_on_06-Apr-2020.csv')
print(df)

df.to_excel('dividend.xlsx')

dividend = pd.read_excel('dividend.xlsx')
print(dividend)


