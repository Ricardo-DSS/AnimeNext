
# import json
# O comando abaixo pode ser utilizado para imprimir no console uma vizualização melhor
# print(json.dumps(dadosApi, sort_keys=False, indent=4))
import webbrowser
import random
from termcolor import colored  # pip install termcolor
from googletrans import Translator  #pip3 install googletrans==3.1.0a0
from jikanpy import Jikan  #pip install jikanpy no terminal
import pywhatkit  #pip3 install pywhatkit

tradutor = Translator()
jikan = Jikan()

def procurar(identificador):
    dadosApi = jikan.anime(identificador, page=1)

    # A condição abaixo evita o retorno de resultados diferentes como filmes, especiais, OVA etc
    if dadosApi["type"] == "TV":
        titulo = dadosApi["title"]
        url = dadosApi["image_url"]
        ep = dadosApi["episodes"]
        sinopse = str(dadosApi["synopsis"]).replace('[Written by MAL Rewrite]', ' ')
        sinopse = tradutor.translate(sinopse, dest="pt")
        sinopseLinha = (sinopse.text).split(".")
        openings = dadosApi["opening_themes"]

        print(colored('\n\nAnime: {}', 'yellow', attrs=['bold', 'dark']).format(titulo))
        print('Episódios: {}'.format(ep))
        print(colored('Sinopse: ', 'yellow'))
        for i in range(0, len(sinopseLinha)):
            print(sinopseLinha[i])
        print('\nOpening: {}'.format(openings[0]))

        if not openings:
            print('Não há abertura')
        else:
            webbrowser.open(url)
            abertura = titulo + ' opening'
            pywhatkit.playonyt(abertura)
    else:
        genero(tipoAnime, pagina)

def genero(tipoAnime, pagina):
    dadosApi = jikan.genre("anime", genre_id=tipoAnime, page=pagina)
    dados = dadosApi["anime"]

    posicaoAnime = random.randint(0, 99)
    anime = dados[posicaoAnime]
    identificador = int(anime["mal_id"])
    procurar(identificador)

def instancia(opcaoGenero, opcaoFama):
    # Pode ser necessário usar o método genero mais de uma vez
    # portanto na primeira vez irei armazenar as variaveis da control
    # nas variáveis globais abaixo

    global tipoAnime
    global pagina

    # O dicionário abaixo converte a opcao do usuario (keyWord)
    # no cod correto do genero para acessar a API
    dicionario = {
        1: 1,
        2: 2,
        3: 4,
        4: 5,
        5: 7,
        6: 8,
        7: 10,
        8: 22,
        9: 24,
        10: 27,
        11: 30,
        12: 36,
        13: 37
    }

    tipoAnime = dicionario.get(opcaoGenero)
    pagina = opcaoFama
    genero(tipoAnime, pagina)