#%%
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

#%%

baseUrl = "https://www.vivareal.com.br/"
url = f"{baseUrl}venda/parana/curitiba/?pagina=" + "{}"

#%%
i=1
ret = requests.get(url.format(i))
soup = bs(ret.text, features="html.parser")
houses = soup.find_all("a", {"class":"property-card__content-link js-card-title"})
qtd_imoveis = int(soup.find("strong", {"class":"results-summary__count js-total-records"}).text.strip().replace(".",""))

#%%
df = pd.DataFrame(
    columns=[
        "descricao",
        "endereco",
        "area",
        "condominio",
        "quartos",
        "wc",
        "vagas",
        "valor",
        "wlink"
    ]
)

i = 0

#%%
while qtd_imoveis > df.shape[0]:
    i += 1
    print(f"valor i: {i} \t\t qtd_imoveis: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text, features="html.parser")
    houses = soup.find_all("a", {"class":"property-card__content-link js-card-title"})
    
    for house in houses:
        try:
            descricao = soup.find("span", {"class":"property-card__title js-cardLink js-card-title"}).text.strip()
        except:
            descricao = None
        try:
            endereco = soup.find("span", {"class":"property-card__address"}).text.strip()
        except:
            endereco = None
        try:
            area = soup.find("span", {"class":"js-property-card-detail-area"}).text.strip()
        except:
            area = None
        try:
            condominio = soup.find("strong", {"class":"js-condo-price"}).text.strip()
        except:
            condominio = None
        try:
            quartos = soup.find("li", {"class":"js-property-detail-rooms"}).span.text.strip()
        except:
            quartos = None
        try:
            wc = soup.find("li", {"class":"js-property-detail-bathroom"}).span.text.strip()
        except:
            wc = None
        try:
            vagas = soup.find("li", {"class":"js-property-detail-garages"}).span.text.strip()
        except:
            vagas = None
        try:
            valor = soup.find("div", {"class":"js-property-card__price-small"}).p.text.strip()
        except:
            valor = None
        try:
            wlink = baseUrl + house["href"]
        except:
            wlink = None
        
        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            condominio,
            quartos,
            wc,
            vagas,
            valor,
            wlink
        ]

