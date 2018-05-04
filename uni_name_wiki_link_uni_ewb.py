try:
    import requests
    import re
    import pandas as pd
    from bs4 import BeautifulSoup

    rr = requests.get("https://en.wikipedia.org/wiki/List_of_universities_in_Bangladesh")
    cc = rr.content
    soup = BeautifulSoup(cc,"html.parser")

    #public university list table
    tables = soup.find("table")
    table_rows = tables.find_all("tr")
    link_dup=''
    info_list=[]
    for tr in table_rows:
        data_dic_for_list = {}
        if ((tr.find("a").text) != "Acronym"):
            data_dic_for_list["University_Name"] = tr.find("a").text
            links = tr.find("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))
            wiki_link = "https://en.wikipedia.org"+links["href"]
            data_dic_for_list["wiki_link"] = wiki_link


    #link use link
            rr = requests.get(wiki_link)
            cc = rr.content
            soup = BeautifulSoup(cc,"html.parser")

    #university page table wiki
            tables2 = soup.find("table",{"class":"infobox vcard"})
            try:
                table_rows2 = tables2.find_all("tr")
                for tr2 in table_rows2:
                    university_internal_links = tr2.find("a",{"class":"external text"})
                    if (university_internal_links == None):
                        continue
                    else:
                        uni_link = university_internal_links["href"]
                        if ((uni_link[:7] == "http://") and (len(uni_link) < 40)):
                            data_dic_for_list["uni_web_link"] = uni_link
            except:
                data_dic_for_list["uni_web_link"] = None

#append data dic into list
            info_list.append(data_dic_for_list)
            
#Make dataFrame and save into csv file.
    df = pd.DataFrame(info_list)
    df.to_csv("university_information_list.csv")

except:
    print("Internet Connection Failed!")
