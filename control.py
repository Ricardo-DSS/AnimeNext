import mal
from termcolor import colored

def menu():
    print(colored('Você deseja ver algo com: ', 'blue', attrs=['bold']) +
          '\n\n1. Ação' +
          '\n2. Aventura' +
          '\n3. Comédia' +
          '\n4. Vanguarda' +
          '\n5. Mistério' +
          '\n6. Drama' +
          '\n7. Fantasia' +
          '\n8. Romance' +
          '\n9. Ficção Científica' +
          '\n10. Shounen' +
          '\n11. Esportes' +
          '\n12. Slice of life' +
          '\n13. Sobrenatural')
    opcaoGenero = input(colored('\nDica! ', 'red', attrs=['bold']) + 'Digite um número de gênero válido ou o programa não funciona!: ')

    while not (opcaoGenero.isdigit()) or not (1 <= int(opcaoGenero) <= 13):
        opcaoGenero = input(colored('Atenção! Você deve escolher um número entre as opções acima (N° 1 a 13): ', 'red', attrs=['bold']))

    print(colored('\nVocê prefere algo: ', 'blue', attrs=['bold']) +
          '\n\n1. Muito popular' +
          '\n2. Popular' +
          '\n3. Conhecido' +
          '\n4. Pouco conhecido' +
          '\n5. Praticamente desconhecido')
    opcaoFama = input(colored('\nLembre-se! Escolha um número entre as opções acima!: ', 'red', attrs=['bold']))

    while not (opcaoFama.isdigit()) or not (1 <= int(opcaoFama) <= 5):
        opcaoFama = input('Ei! A opção deve ser um número entre 1 e 5: ')

    # As validações foram feitas como string, portanto aqui fica garantido
    # que os parâmetros irão funcionar como o esperado em INT
    opcaoGenero = int(opcaoGenero)
    opcaoFama = int(opcaoFama)
    mal.instancia(opcaoGenero, opcaoFama)

    print(colored('\n\nNão gostou? Deseja tentar novamente?', 'cyan', attrs=['bold']) +
          '\nDigite ' + colored('1', 'cyan', attrs=['bold']) + ' para receber outra recomendação ' +
          'ou qualquer outra tecla para ' + colored('SAIR: ', 'cyan', attrs=['bold']))
    again = input()
    if again == '1':
        menu()
    else:
        quit()

