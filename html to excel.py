import pandas as pd
import html5lib

url = 'https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/large-cap-fund.html'

tables_on_page = pd.read_html(url)
print(tables_on_page)
print(type(tables_on_page))

tables = tables_on_page[0]
print(type(tables))

print(tables)


tables.to_excel('large_cap_analysis.xlsx')
print('large_cap_analysis.xlsx')

# For printing, we need to read table into a new variable as a direct
# print statement to the name of the table can't print the table only
# the string of its name.

output = pd.read_excel('large_cap_analysis.xlsx')
print(output)

