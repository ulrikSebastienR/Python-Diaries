from nsetools import Nse

nse = Nse()
print(nse)

#https://nsetools.readthedocs.io/en/latest/usage.html#instantiation

q = nse.get_quote('infy')
print(q)

print(nse.get_index_list(), 'r', sep ='\n')

print(nse.get_index_quote("nifty pharma"))

p = nse.get_index_quote("nifty pharma")
print("p=" ,p)
print(type(p))





