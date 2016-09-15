howfrom bs4 import BeautifulSoup
import urllib
import sys
import psycopg2


class record:
    def __init__(self,name,regno,city,state,chief,address,sectors):
        self.name = name
        self.regno = regno
        self.city = city
        self.state = state
        self.chief = chief
        self.address = address
        self.sectors = sectors



MAX_RECORDS = 65535    # this number should be set to maximum in order to remove multiple pages

SCRAPE_URL = "http://ngo.india.gov.in/state_ngolist_ngo.php?records="+str(MAX_RECORDS)+"&state_value="+sys.argv[1]

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




    #regno = row.findAll("td")[2].text.strip()
    #city = row.findAll("td")[1].text.strip()
    #state = row.findAll("td")[1].text.strip()

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

