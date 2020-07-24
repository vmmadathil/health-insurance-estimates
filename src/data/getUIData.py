import urllib.request
import datetime

#starting date
startDate = datetime.datetime.strptime("03/07/20", "%m/%d/%y")

#ending date
endingDate = datetime.datetime.strptime("03/07/20", "%m/%d/%y")

currDate = startDate

#iterating through 
while (currDate <= endingDate):
    currString = (currDate.strftime("%m/%d/%y")).replace('/', '') 
    page = urllib.request.urlopen("https://oui.doleta.gov/unemploy/page8/2020/" + currString + ".html")
    pageBytes = page.read()

    pageStr = pageBytes.decode("utf8")
    page.close()

    print(pageStr)
    currDate = currDate + datetime.timedelta(days=5)

