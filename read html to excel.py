import pandas as pd

df = pd.read_html("https://www.motilaloswalmf.com/nav/latest-nav/motilal-oswal-MOSt-focused-25-fund/MO19233")
print(df)

df.to_csv('mo.csv')
