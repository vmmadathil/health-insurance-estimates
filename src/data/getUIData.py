import urllib.request
import datetime
import re
import pandas as pd
#starting date
startDate = datetime.datetime.strptime("03/07/20", "%m/%d/%y")

#ending date
endingDate = datetime.datetime.strptime("03/07/20", "%m/%d/%y")

currDate = startDate

#iterating through 
while (currDate <= endingDate):
    currString = (currDate.strftime("%m/%d/%y")).replace('/', '') 
    url = "https://oui.doleta.gov/unemploy/page8/2020/" + currString + ".html"
    tables = pd.read_html(url, header=None)
    table = tables[0]

    table = table.iloc[0:, : 4]
    table.columns = table.columns.droplevel([-1, -2, -3]) 
    
    table = table.rename(columns = {'STATENAME' : 'State', 'Initial Claims Filed During Week Ended  March 7, 2020' : 'Initial Claims', 'Initial Claims Filed During Week Ended  March 7, 2020' : 'Change From Last Week', 'Initial Claims Filed During Week Ended  March 7, 2020' : 'Change From Last Year'})
    print(table)

    
    currDate = currDate + datetime.timedelta(days=5)

