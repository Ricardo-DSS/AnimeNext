import pandas as pd
import json
import random
from googletrans import Translator # pip3 install googletrans==3.1.0a0
from jikanpy import Jikan # pip install jikanpy no terminal

tradutor = Translator()
jikan = Jikan()

def procurar(iden, sinopse):
    dadosApi = jikan.search('anime', iden, page=1)
    # print(json.dumps(dadosApi, sort_keys=False, indent=4))

    dados = dadosApi["results"]
    # print(json.dumps(dados, sort_keys=False, indent=4))

    df = pd.DataFrame.from_dict(dados)
    #print(df)
    analise = df.index[df['title'] == iden].tolist()
    linha = analise[0]
    print('Anime: ', iden)
    print('Episódios: ', str(df.iat[linha, 7]))
    sinopse = tradutor.translate(sinopse, dest="pt")
    print('Sinopse: ', sinopse.text)
    print('imagem: ', str(df.iat[linha, 2]))

def genero(opcao):
    dadosApi = jikan.genre('anime', genre_id=opcao)
    # print(json.dumps(dadosApi, sort_keys=False, indent=4))

    dados = dadosApi["anime"]
    print(json.dumps(dados, sort_keys=False, indent=4))

    posicaoAnime = random.randint(0, 99)
    anime = dados[posicaoAnime]
    iden = str(anime["title"])
    sinopse = str(anime["synopsis"]).replace('\r\n\r\n[Written by MAL Rewrite]', ' ')
    # print(json.dumps(anime, sort_keys=False, indent=4))
    procurar(iden, sinopse)
