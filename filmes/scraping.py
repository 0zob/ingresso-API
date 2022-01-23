import asyncio
import requests
from bs4 import BeautifulSoup
from pyppeteer import launch 


def filmes_em_alta() -> list:
    filmes_em_alta = []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    carrosel = soup.find(class_='em-alta carousel-box')
    filmes = carrosel.find_all('article')

    for filme in filmes:
        filmes_em_alta.append(filme.get_text().strip())

    return filmes_em_alta

def filmes_em_cartaz() -> list:
    filmes_em_cartaz= []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    carrosel = soup.find(class_='em-cartaz carousel-box')
    filmes = carrosel.find_all('article')

    for filme in filmes:
        filmes_em_cartaz.append(filme.get_text().strip())

    return filmes_em_cartaz

async def get_filmes():
    browser = await launch(
    handleSIGINT=False,
    handleSIGTERM=False,
    handleSIGHUP=False,
    headless=True,
    args=['--no-sandbox'],

    )
    page = await browser.newPage()
    await page.goto('https://www.ingresso.com/filmes?city=sao-paulo&partnership=home', {'waitUntil' : 'networkidle2'})
    page_content = await page.content() 

    await browser.close()

    return page_content

def filmes() -> list:
    todos_filmes = []

    page = asyncio.run(get_filmes())
    soup = BeautifulSoup(page, 'html.parser')

    filmes = soup.find_all(class_='card ing-small')

    for filme in filmes:
        caracteristicas = {}

        caracteristicas['titulo'] = filme.get_text().strip()

        img = filme.find('img')
        caracteristicas['img'] =  img['src'].strip()

        todos_filmes.append(caracteristicas.copy())

    return todos_filmes

def filme_principal() -> dict:
    filme = {}

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    banner = soup.find_all(class_='main-home-banner')[1]
    
    titulo = banner.get_text().strip()

    titulo = titulo.split('\n')
    filme['titulo'] = titulo[0] 

    picture = banner.find('picture')
    source = picture.find('source')
    filme['img'] = source['srcset']

    return filme

def noticias() -> list:
    noticias = []

    page = requests.get('https://www.ingresso.com/home?city=sao-paulo&partnership=home')
    soup = BeautifulSoup(page.text, 'html.parser')

    noticias_html = soup.find_all(class_='news-h-article')

    for noticia in noticias_html:
        caracteristicas = {}

        img = noticia.find('img')

        caracteristicas['img'] = img['src']

        caracteristicas['titulo'] = noticia.find('h2').get_text()
        caracteristicas['descricao'] = noticia.find('p').get_text()

        noticias.append(caracteristicas.copy())

    return noticias
