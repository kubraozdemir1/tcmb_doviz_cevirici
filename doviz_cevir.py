# TCMB sitesinden efektif dolar satış fiyatını çekelim.
# https://www.turkiye.gov.tr/doviz-kurlari

from bs4 import *
import requests

sayfa = requests.get("https://www.turkiye.gov.tr/doviz-kurlari")

#print(sayfa.text)

soup = BeautifulSoup(sayfa.text, "html.parser")

efektif_dolar_satis = soup.find('td', text='1 ABD DOLARI')\
                          .find_next_sibling('td')\
                          .find_next_sibling('td')\
                          .find_next_sibling('td')\
                          .text

print('efektif_dolar_satis', efektif_dolar_satis)







