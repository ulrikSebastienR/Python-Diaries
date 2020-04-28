#importing html table into pandas https://www.youtube.com/watch?v=VhPCnhYcklI

import pandas as pd
#import html5lib
url = 'http://floodobservatory.colorado.edu/Archives/MasterListrev.htm'

table = pd.read_html(url, header = 0)
print(type(table))
#print(table)
print(table[0])



