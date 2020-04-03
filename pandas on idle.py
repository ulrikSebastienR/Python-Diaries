import pandas as pd


excel1 = 'worksheet1.xlsx'
print(excel1)

excel2 = 'worksheet2.xlsx'
print(excel2)

excel3 = 'worksheetodf.xlsx'
print(excel3)

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)

merge = pd.merge(df1,df2,on ="Date")
print(merge)

merge.to_excel("output.xlsx")
output_sheet = 'output.slsx'
dfoutput = pd.read_excel(output_sheet)




