import mal

def menu():
    print('Você deseja ver algo com: ' +
          '\n1. Ação' +
          '\n2. Aventura' +
          '\n3. Carros' +
          '\n4. Comédia' +
          '\n5. Vanguarda' +
          '\n6. Demônios' +
          '\n7. Mistério')
    opcao = int(input())
    mal.genero(opcao)

