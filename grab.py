import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

#make your date range, make same day for 1 day
d1 = date(2018, 7, 10)  # start date year,month,date
d2 = date(2018, 7, 12)  # end date year,month,date

delta = d2 - d1         # timedelta

localsave="calltime,dispatchtime,incidentdesc,disposition,eventnumber,location,priority,case\n"
    
for i in range(delta.days + 1):
    grabthisday = (d1 + timedelta(i)) #1day at a time cause 250 limit on search results
    print(grabthisday)
    payload = {'DateFrom': grabthisday, 'DateThrough': grabthisday, 'EventNumberFilterOption': 'IsExactly','StreetNumberFilterOption': 'IsExactly','StreetNameFilterOption': 'IsExactly','CaseNumberFilterOption': 'IsExactly'
     } 
    r = requests.post(url="http://coeapps.eugene-or.gov/EPDDispatchLog/Search", data=payload)
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find_all('table')[1] 

    rows = table.find_all('tr')[2:]

    calltime=[]
    dispatchtime=[]
    incidentdesc=[]
    disposition=[]
    eventnumber=[]
    location=[]
    priority=[]
    case=[]

    for row in rows:
        cols = row.find_all('td')
        calltime.append( cols[1].get_text() )
        dispatchtime.append( cols[2].get_text() )
        incidentdesc.append( cols[3].get_text() )
       

        disposition.append( cols[4].get_text() )
        eventnumber.append( cols[5].get_text() )
        

        location.append( cols[6].get_text() )

        priority.append( cols[7].get_text() )
        case.append( cols[8].get_text() )
        localsave+=cols[1].get_text()+","+cols[2].get_text()+",\""+cols[3].get_text()+"\","+cols[4].get_text()+","+cols[5].get_text()+",\""+cols[6].get_text()+"\","+cols[7].get_text()+","+cols[8].get_text()+"\n"

print (localsave)
f = open('crime.csv','w')
f.write(localsave)
f.close()

#copyleft
