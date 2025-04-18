import requests
from bs4 import BeautifulSoup
from settings import url, headers
import json


def get_universal_html():
	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		print("respuesta exitosa")
		return response.text 
	else:
		print("error en la solicitud")
		return None

def universal_parsel():
	lista = []
	html_content = get_universal_html()
	soup = BeautifulSoup(html_content, "html.parser")
	if not html_content:
		print("Not html")
		return
	noticias = soup.find_all('li', class_=lambda c: c and 'relative' in c)
	print(f"Se encontraron {len(noticias)} noticias")

	for id, noticia in enumerate(noticias, start = 1):
		title_tag = noticia.find('h2')
		title = title_tag.get_text(strip = True) if title_tag else "no title"
		description_tag = noticia.find('p',class_ = lambda c: c and 'summary' in c)
		description = description_tag.get_text(strip = True) if description_tag  else "no description"
		lista.append({
			"id": id,
			"title": title,
			"description": description
			})
	return lista

universal_news = universal_parsel()

with open("universal_news.json", "w", encoding = "utf-8") as f:
	json.dump(universal_news, f, ensure_ascii = False, indent = 4)

