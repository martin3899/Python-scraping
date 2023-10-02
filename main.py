import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import json

url = 'https://www.leagueofgraphs.com/fr/champions/items'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)


if response.ok:
    soup = BeautifulSoup(response.text)
    table = soup.find('table',id='topItemsTable')
    trs = table.find_all('tr')
    obj= []
    for tr in trs[1:-1]:
        tds=tr.find_all('td')
        name = tds[0].img["alt"]
        popularity = tds[1].progressbar["data-value"]
        percentVictory = tds[2].progressbar["data-value"]
        obj.append(
            {
                "nom" : name,
                "popularité" :round(float(popularity)*100,2),
                "Pourçentage de victoire" : round(float(percentVictory)*100,2)
            }
        )



    # obj.sort(key=lambda x: x.get('nom'))
    # obj.sort(key=lambda x: x.get('popularité'), reverse=True)
    obj.sort(key=lambda x: x.get('Pourçentage de victoire'), reverse=True)
    # print(obj)

    df=pd.DataFrame(obj)
    plt.plot(df["Pourçentage de victoire"],df["popularité"])
    plt.show()
    print(df)




