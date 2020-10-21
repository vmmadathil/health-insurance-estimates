import censusdata

x= censusdata.search('acs5', 2015, 'label', 'unemploy')[160:170]

print(x)