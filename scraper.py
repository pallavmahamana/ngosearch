from bs4 import BeautifulSoup
import urllib
import sys
from pymongo import MongoClient


class record:
    def __init__(self,name,regno,city,state,chief,address,sectors):
        self.name = name
        self.regno = regno
        self.city = city
        self.state = state
        self.chief = chief
        self.address = address
        self.sectors = sectors

def scrapestate(SC):
    SCRAPE_URL = "http://ngo.india.gov.in/state_ngolist_ngo.php?records=65535&state_value="+SC

    r = urllib.urlopen(SCRAPE_URL).read()
    soup = BeautifulSoup(r)

    table = soup.find("table",{"width":"100%","border":"0","align":"center","cellspacing":"0","cellpadding":"5"})
    rows = table.findAll("tr")

    statename = soup.findAll("strong")[2].text
    statename = statename[0:statename.find("(")].strip()

    cleanrows=[]

    # this will clean the rows
    for row in rows:
        if len(row.findAll("td",{"valign":"top"})) == 6:
            cleanrows.append(row)


    recordlist = []

    for row in cleanrows:
        name = row.findAll("td")[1].text.strip()
        str = row.findAll("td")[2].text

        cities = []
        cp = []
        for i in range(len(str)):
            if str[i] == ',':
                cp.append(i)

        for i in cp:
            pos = str.rfind(')',0,i)
            if pos != -1:
                cities.append(str[str.rfind(')',0,i)+1:i].strip())


        cities = filter(None,list(set(cities)))

        regno = []
        str = row.findAll("td")[2].text.strip()

        regno.append(str[:str.find("(")].strip())

        while str.find(statename) != -1:
            str = str[str.find(statename)+len(statename):]
            regno.append(str[0:str.find("(")].strip())

        regno = filter(None,regno)

        chief = row.findAll("td")[3].text.strip()
        address = row.findAll("td")[4].text.strip()
        sectors = row.findAll("td")[5].text.strip().split(',')

        obj = record(name,regno,cities,statename,chief,address,sectors)
        recordlist.append(obj)

    return recordlist

client = MongoClient()
db = client.test
statecode = ["AN","AP","AR","AS","BR","CH","CG","DN","DD","DL","GA","GJ","HR","HP","JK","JH","KA","KL",
"LD","MP","MH","MN","ML","MZ","NL","OR","PY","PB","RJ","SK","TN","TR","UP","UA","WB"]

for SC in statecode:
    records = scrapestate(SC)
    
    for i in records:
        db.ngodata.insert_one(i.__dict__)
    print len(records),"records written for",SC
