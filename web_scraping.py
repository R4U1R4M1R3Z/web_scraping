import requests
from bs4 import BeautifulSoup
import re

with open('C:\\Users\URL_EXPORT.txt', 'w', encoding='utf-8') as f:
    cont = 0
    ##introducir numero de paginas
    for i in range(1, 48):
        url = 'https://pagina_prueba.com'+str(i)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        cards = soup.select('div.col-md-8')

        for card in cards:
            h2_tag = card.select_one('h2.card-title')  
            price_tag = card.select_one('span.meta-price')  
            year_tags = card.select('span.meta')  

            year_tag = None
            for tag in year_tags:
                if re.fullmatch(r'\d{4}', tag.get_text().strip()):
                    year_tag = tag
                    break
            #introducir etiquetas a buscar. 
            title = h2_tag.get_text().strip() if h2_tag else None
            price = price_tag.get_text().strip() if price_tag else None
            year = year_tag.get_text().strip() if year_tag else None

            cont += 1
            f.write(f"Number: {cont} , Title: {title}, Price: {price}, Year: {year}\n")
