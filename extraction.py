#%%
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

#%%

baseUrl = "https://www.vivareal.com.br/"
url = f"{baseUrl}venda/parana/curitiba/?pagina=" + "{}"

