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

