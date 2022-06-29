
global genre
global pagina

import json
import random
from googletrans import Translator  #pip3 install googletrans==3.1.0a0
from jikanpy import Jikan  #pip install jikanpy no terminal
import pywhatkit  #pip3 install pywhatkit

tradutor = Translator()
jikan = Jikan()

def procurar(identificador):
    openings = []

    dadosApi = jikan.anime(identificador, page=1)
    # print(json.dumps(dadosApi, sort_keys=False, indent=4))

    # A condição abaixo evita o retorno de resultados diferentes como filmes, especiais etc
    if dadosApi["type"] == "TV":
        titulo = dadosApi["title"]
        url = dadosApi["image_url"]
        ep = dadosApi["episodes"]
        sinopse = str(dadosApi["synopsis"]).replace('[Written by MAL Rewrite]', ' ')
        sinopse = tradutor.translate(sinopse, dest="pt")
        openings = dadosApi["opening_themes"]

        print('Anime: {}'.format(titulo))
        print('Episódios: {}'.format(ep))
        print('Sinopse: {}'.format(sinopse.text))
        print('Imagem: {}'.format(url))
        print('Opening: {}'.format(openings[0]))

        if not openings:
            print('Não há abertura')
        else:
            abertura = titulo + ' opening'
            pywhatkit.playonyt(abertura)
    else:
        genero(genre, pagina)

def genero(genre, pagina):
    dadosApi = jikan.genre("anime", genre_id=genre, page=pagina)
    # print(json.dumps(dadosApi, sort_keys=False, indent=4))

    dados = dadosApi["anime"]
    # print(json.dumps(dados, sort_keys=False, indent=4))

    posicaoAnime = random.randint(0, 99)
    anime = dados[posicaoAnime]
    identificador = int(anime["mal_id"])
    # print(json.dumps(anime, sort_keys=False, indent=4))
    procurar(identificador)

def instancia(opcaoGenero, opcaoFama):
    '''Pode ser necessário usar o método genero mais de uma vez
    portanto na primeira vez irei armazenar as variaveis da control
    nas variáveis globais abaixo'''
    genre = opcaoGenero
    pagina = opcaoFama
    genero(genre, pagina)