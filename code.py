from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

data = requests.get(url)

beatifulSoup = BeautifulSoup(data.text, "html.parser") 
table = beatifulSoup.find('table')

tempList = []
trTag = table.find_all('tr')

for tr in trTag:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

names = []
radius = []
mass = []
distance = []

tempListLen = len(tempList)

for i in range(1,tempListLen):
    names = (tempList[1])
    radius = (tempList[6])
    mass = (tempList[5])
    distance = (tempList[3])

df = pd.DataFrame(list(zip(names,radius,mass,distance)),columns=['Name','Radius','Mass','Distance'])
df.to_csv('stars.csv')
