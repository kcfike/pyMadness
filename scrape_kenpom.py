#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
import pdb

wiki = "https://kenpom.com/"
page = urlopen(wiki)
soup = BeautifulSoup(page, "html5lib")
ratings_table=soup.find('table', id='ratings-table')

IDX=[]
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
M=[]
index=0
for row in ratings_table.findAll("tr"):
    col=row.findAll('td')
    if len(col)>0:
        index+=1
        IDX.append(index)
        A.append(col[0].find(text=True))
        B.append(col[1].find(text=True))
        C.append(col[2].find(text=True))
        D.append(col[3].find(text=True))
        E.append(col[4].find(text=True))
        F.append(col[5].find(text=True))
        G.append(col[7].find(text=True))
        H.append(col[9].find(text=True))
        I.append(col[11].find(text=True))
        J.append(col[13].find(text=True))
        K.append(col[15].find(text=True))
        L.append(col[17].find(text=True))
        M.append(col[19].find(text=True))

df=pd.DataFrame(IDX,columns=['Index'])
df['Rank']=A
df['Team']=B
df['Conf']=C
df['W-L']=D
df['AdjEM']=E
df['AdjO']=F
df['AdjD']=G
df['AdjT']=H
df['Luck']=I
df['AdjEMSOS']=J
df['OppOSOS']=K
df['OppDSOS']=L
df['AdjEMNCSOS']=M

with open('kenpom.json', 'w') as f:
    f.write(df.to_json(orient='index'))
