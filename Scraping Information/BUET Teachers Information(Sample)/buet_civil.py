import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

url = "http://ce.buet.ac.bd/faculty.htm#ee"

result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,"html.parser")

tables = soup.find("table")
rows = tables.findAll("tr")
l = []
for tr in rows:
    d = {}
    try:
        d["member_name"] = tr.find("a").find(text=True).strip()
        td = tr.find("a").find(text=True).strip()
        try:
            #d["faculty_designation"] = tr.find("p").findAll(text=True)[1].strip()
            designation = tr.find("p").findAll(text=True)[1].strip()
            try:
                #d["faculty_designation"] = tr.find("p").findAll(text=True)[2].strip()
                designation = tr.find("p").findAll(text=True)[2].strip()
                try:
                    #Clear empty space and reformation
                    #d["faculty_designation"] = tr.find("p").findAll(text=True)[3].strip()
                    designation = tr.find("p").findAll(text=True)[3].strip()
                except:
                    pass
            except:
                pass
        except:
            pass
        if (td == None):
            continue
        print(td)
        print(designation)
        #l.append(d)
        
    except:
        pass
    
#df = pd.DataFrame(l)
#df.to_csv("buet_civil.csv")
