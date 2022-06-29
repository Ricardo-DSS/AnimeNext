import mal

def menu():
    print('Você deseja ver algo com: ' +
          '\n1. Ação' +
          '\n2. Aventura' +
          '\n4. Comédia' +
          '\n5. Vanguarda' +
          '\n7. Mistério' +
          '\n8. Drama' +
          '\n10. Fantasia' +
          '\n22. Romance' +
          '\n24. Ficção Científica' +
          '\n27. Shounen' +
          '\n30. Esportes' +
          '\n36. Slice of life' +
          '\n37. Sobrenatural')
    opcaoGenero = int(input())
    print('Você prefere algo: ' +
          '\n1. Muito popular' +
          '\n2. Popular' +
          '\n3. Conhecido' +
          '\n4. Pouco conhecido' +
          '\n5. Praticamente desconhecido')
    opcaoFama = int(input())
    mal.instancia(opcaoGenero, opcaoFama)

