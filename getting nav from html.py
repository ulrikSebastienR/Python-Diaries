import pandas as pd
import html5lib

url = "https://www.moneycontrol.com/mutual-funds/nav/franklin-india-feeder-franklin-u-s-opportunities-fund-direct-dividend/MTE306"

lists = pd.read_html(url)
print(lists)


