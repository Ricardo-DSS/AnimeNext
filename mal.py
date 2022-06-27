import pandas as pd
import json
import random
from jikanpy import Jikan # pip install jikanpy no terminal
jikan = Jikan()



def procurar():
    dadosApi = jikan.search('anime', 'Naruto', page=1)
    # print(json.dumps(dadosApi, sort_keys=False, indent=4))

    dados = dadosApi["results"]
    # print(json.dumps(dados, sort_keys=False, indent=4))

    df = pd.DataFrame.from_dict(dados)
    analise = df.index[df['title']=='Naruto'].tolist()
    linha = analise[0]
    identificador = (df['mal_id'].values[linha])
    return identificador

def genero():
    dadosApi = jikan.genre('anime', genre_id=4)
    # print(json.dumps(dadosApi, sort_keys=False, indent=4))

    dados = dadosApi["anime"]
    # print(json.dumps(dados, sort_keys=False, indent=4))

    posicaoAnime = random.randint(0, 99)
    anime = dados[posicaoAnime]
    print(json.dumps(anime, sort_keys=False, indent=4))
    titulo = str(anime["title"])
    sinopse = str(anime["synopsis"])
    episodios = str(anime["episodes"])

    #print('O anime recomendado é: ', titulo)
    print(sinopse.replace('\r\n\r\n[Written by MAL Rewrite]', ' ',))
    #print('Quantidade de episódios', episodios)
