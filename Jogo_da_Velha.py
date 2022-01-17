""" Programa Jogo da velha"""


# Importação da biblioteca os
import os

""" Funções """

# Função que inicia o jogo, cria o tabuleiro e cria o contadooor de jogadas
def inicio():

    tab = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n_jogadas = 0
    return tab, n_jogadas


# Função que recebe os valores digitados pelo usuários e faz a validação desses valores
def digita_jogada():

    lista_jogadas = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    jogada = input('Digite o número da posição onde deseja jogar: ')
    if jogada in lista_jogadas:
        return int(jogada)
    elif jogada == 'sair':
        print(' ' * 19 + f'{red}Fim do Jogo!{reset}')
        exit(2)
    else:
        print(' ' * 17 + f'{red}Valor Incorreto{reset}')
        return digita_jogada()


# Função que imprime o tabuleiro
def print_tabuleiro(tab):

    print('-'*18 +'Jogo da Velha!' + '-'*18)
    print('\n')
    for j in tab:
        print(' '*19, end='')
        for i in j:
            if i == 'X':
                print(f'[{amarelo}{i}{reset}] ', end='')  # Imprime as jogadas do 'X' em amarelo
            elif i == 'O':
                print(f'[{blue}{i}{reset}] ', end='')  # Imprime as jogadas do 'O' em azul
            else:
                print(f'[{cinza}{i}{reset}] ', end='')  # Imprime as posições sem jogadas em cinza
        print('')
    print('\n')
    print('-'*50)
    print(' '*9 + "Para sair do jogo digite 'sair'!")
    print('-'*50)


# Função que imprime o vencedor
def venceu():

    print('')
    print(f' '*10 + f'{red}!!! O jogador{reset}{amarelo}[ X ]{reset}{red}venceu !!!{reset}') if (n_jogadas - 1) % 2 == 0 \
        else print(f' '*10 + f'{red}!!! O jogador{reset}{blue}[ 0 ]{reset}{red}venceu !!!{reset}')
    return True


# Função que faz a verificação da condição de vitória
def verifica_jogo(tab):

    # variáveis para comparação das jogadas nas linhas
    lista_X = ['X', 'X', 'X']
    lista_O = ['O', 'O', 'O']

    """ Veerificação do jogador X"""
    # verifica todas as posições para o jogador 'X'
    if (tab[0][0:] == lista_X or tab[1][0:] == lista_X or tab[2][0:] == lista_X) \
        or (tab[0][0] == 'X' and tab[1][0] == 'X' and tab[2][0] == 'X') \
        or (tab[0][1] == 'X' and tab[1][1] == 'X' and tab[2][1] == 'X') \
        or (tab[0][2] == 'X' and tab[1][2] == 'X' and tab[2][2] == 'X') \
        or (tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X') \
        or (tab[0][2] == 'X' and tab[1][1] == 'X' and tab[2][0] == 'X'):
        return venceu()

    """ Verificação do jogador O"""
    # verifica todas as posições para o jogador 'O'
    if (tab[0][0:] == lista_O or tab[1][0:] == lista_O or tab[2][0:] == lista_O) \
        or (tab[0][0] == 'O' and tab[1][0] == 'O' and tab[2][0] == 'O') \
        or (tab[0][1] == 'O' and tab[1][1] == 'O' and tab[2][1] == 'O') \
        or (tab[0][2] == 'O' and tab[1][2] == 'O' and tab[2][2] == 'O') \
        or (tab[0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O') \
        or (tab[0][2] == 'O' and tab[1][1] == 'O' and tab[2][0] == 'O'):
        return venceu()

    # Condição que verifica se já se esgotou as jogadas possíveis
    if n_jogadas == 9:
        os.system("cls")
        print()
        print(' '*15 + f'{red}Não houve vencedor !{reset}')
        return True
    return False


# Função que verifica se o jogo irá ser reiniciado
def jogar_de_novo():
    reiniciar = input('Deseja jogar novamente? (s ou n): ')
    if reiniciar == 's':
        os.system("cls")
        t, n = inicio()
        return t, n
    elif reiniciar == 'n':
        print(' ' * 19 + f'{red}Fim do Jogo!{reset}')
        exit(-1)
    else:
        print(f'{red}Valor digitado incorreto. Valores aceitos (s ou n){reset}')
        return jogar_de_novo()


""" Iniciando Jogo """
# Variáveis com os códigos de cores
amarelo = "\033[1;33m"
cinza = "\033[0;37m"
red = "\033[1;31m"
blue = "\033[1;34m"
reset = "\033[m"

# Discionário com as posições do tabuleiro
dicionario = {1: (0, 0),
              2: (0, 1),
              3: (0, 2),
              4: (1, 0),
              5: (1, 1),
              6: (1, 2),
              7: (2, 0),
              8: (2, 1),
              9: (2, 2)}

# Cria tabuleiro e limpa a tela
tab, n_jogadas = inicio()
os.system("cls")

# Loop do Jogo
while True:

    # chama função que irá imprimir o tabuleiro passando o tabuleiro como argumento
    print_tabuleiro(tab)

    # Define qual o jogador da vez
    print(f' '*20 + f'{amarelo}Jogador  X{reset}') if n_jogadas % 2 == 0 \
        else print(f' '*20 + f'{blue}Jogador  O{reset}')

    # Chama função para receber o valor digitados pelos jogadores
    jogada = digita_jogada()

    # Utilizando o valor retornado da função 'digita_jogada, chama a função dicionário, que retornará
    # os valores da linha e coluna para inserção dos valores 'X' ou 'O'.
    linha, coluna = dicionario[jogada]
    if tab[linha][coluna] == 'X' or tab[linha][coluna] == 'O':  # Verifica se já existe a jogada
        os.system("cls")
        print(f' ' * 6 + f'{red}!!! ATENÇÂO: Jogada não permitida !!!{reset}')
    else:
        if n_jogadas % 2 == 0:  # Verifica qual dos jogadores esta na vez para inserção do novo valor
            tab[linha][coluna] = 'X'
        else:
            tab[linha][coluna] = 'O'
        n_jogadas += 1
        os.system("cls")

    # Chama a função para verificar se houve um vencedo
    if verifica_jogo(tab):
        print_tabuleiro(tab)   # mostra o tabulerio com a jogada vencedora
        tab, n_jogadas = jogar_de_novo()  # Função verifica se o jogo será reiniciado