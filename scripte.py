import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import csv
# les varible n'assicer
jour=15
mois=6
Dectionner={
    'date':[],
    'equipe A':[],
    'equipe B':[],
    'Score':[],
}
# cette boucule a comme objectif de scropier tous les matche de débute de matche jusque la fine de coupe de monde
while jour !=14 :

    date = f'2025-0{mois}-{jour}' if jour > 10 else f'2025-0{mois}-0{jour}'
    #le site qui on scrope
    url=f"https://www.footmercato.net/live/{date}"
    rsp=requests.get(url)
    soup=BeautifulSoup(rsp.text,'html.parser')
    # la prtie en page qui contient tous les matche de monde
    matches_Goup=soup.find_all('div',class_='matchesGroup')
    for matches in matches_Goup:
            # donne cette étape en spisifier les matche de coupe de monde
            if matches.find('div',class_='title').text.strip()=="Coupe du monde des clubs FIFA":
                matche_Coup=matches.find_all('div',class_="matchesGroup__match")
                # donne cette étape en remplier le dectionner 
                for ele in matche_Coup:
                    Dectionner['date'].append(date)
                    Dectionner['equipe A'].append(ele.find_all('span',class_='matchTeam__name')[0].text)
                    Dectionner['equipe B'].append(ele.find_all('span',class_='matchTeam__name')[1].text)
                    Dectionner['Score'].append(ele.find_all('span',class_='matchFull__score')[0].text+":"+ele.find_all('span',class_='matchFull__score')[1].text)
    if jour<31:
        jour+=1
    else:
        jour=1
        mois=7
df=pd.DataFrame(Dectionner)
# donne cette étape en doit enrgistre les donne en un ficher exeel
fiche='data.csv'
df.to_csv(fiche,index=False)
