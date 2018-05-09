import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

url = "http://cse.buet.ac.bd/faculty/active_fac_short.php"

result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,"html.parser")

members = soup.findAll("div",{"class":"faculty-block"})
#print (info)
l = []
for member in members:
    d = {}
    d["member_name"] = member.find("a").find(text=True)
    d["faculty_designation"] = member.find("p",{"class":"faculty-designation"}).find(text=True)
    l.append(d)

#df = pd.DataFrame(l)
#df.to_csv("buet_cse.csv")
