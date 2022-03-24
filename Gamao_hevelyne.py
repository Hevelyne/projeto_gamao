import random
import os

# Seed para geração aleatória dos números obtidos do sistema
random.seed(os.urandom(1))

PC_CLARA = '\u001b[33;1m●\u001b[0m'  # Círculo amarelo
PC_ESCURA = '\u001b[32;1m●\u001b[0m' # Círculo verde
PC_NULA = '\u001b[37;1m◌\u001b[0m'   # Círculo pontilhado branco
CS_CLARA = '\u001b[34;1m|\u001b[0m'  # Barra azul
CS_ESCURA = '\u001b[31;1m|\u001b[0m' # Barra vermelha
CS_MEIO = '\u001b[37;1m|\u001b[0m'   # Barra branca

# Matriz com os elementos peças distribuídas no tabuleiro
pecas_posi = [[PC_CLARA, PC_CLARA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA], 
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],   [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA],
              [PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA, PC_ESCURA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_CLARA, PC_CLARA, PC_CLARA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], 
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA, PC_CLARA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA],
              [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_NULA, PC_NULA, PC_NULA, PC_NULA, PC_NULA], [PC_ESCURA, PC_ESCURA, PC_NULA, PC_NULA, PC_NULA]]

pecas_retiradas_claras = []*15
pecas_retiradas_escuras = []*15

# Definição da função que printa o tabuleiro e as peças na tela
def Print_Tabuleiro():
    print("\u001b[1m     24   23   22   21   20   19        18   17   16   15   14   13\u001b[0m")
    for linha in range(5):
        print("\u001b[1m", linha+1, "\u001b[0m", end = '')
        for coluna in range(13):
            if coluna == 6:
                print(CS_MEIO, pecas_posi[coluna][linha], CS_MEIO, end = '')
            elif coluna % 2 == 0:
                print(CS_CLARA, pecas_posi[coluna][linha], CS_CLARA, end = '')
            else:
                print(CS_ESCURA, pecas_posi[coluna][linha], CS_ESCURA, end = '')
        print()
    print()
    for linha in range(5, 0, -1):
        print("\u001b[1m", linha, "\u001b[0m", end = '')
        for coluna in range(25, 12, -1):
            if coluna == 19:
                print(CS_MEIO, pecas_posi[coluna][linha-1], CS_MEIO, end = '')
            elif coluna % 2 == 0:
                print(CS_CLARA, pecas_posi[coluna][linha-1], CS_CLARA, end = '')
            else:
                print(CS_ESCURA, pecas_posi[coluna][linha-1], CS_ESCURA, end = '')
        print()
    print("\u001b[1m     01   02   03   04   05   06        07   08   09   10   11   12\u001b[0m\n")

def Dado():
    valor = random.randint(1, 6)
    if valor == 1:
        print(" ---------\n",
              "|       |\n",
              "|   ○   |\n",
              "|       |\n",
              "---------\n")
        return valor
    elif valor == 2:
        print(" ---------\n",
              "|     ○ |\n",
              "|       |\n",
              "| ○     |\n",
              "---------\n")
        return valor
    elif valor == 3:
        print(" ---------\n",
              "|     ○ |\n",
              "|   ○   |\n",
              "| ○     |\n",
              "---------\n")
        return valor
    elif valor == 4:
        print(" ---------\n",
              "| ○   ○ |\n",
              "|       |\n",
              "| ○   ○ |\n",
              "---------\n")
        return valor
    elif valor == 5:
        print(" ---------\n",
              "| ○   ○ |\n",
              "|   ○   |\n",
              "| ○   ○ |\n",
              "---------\n")
    elif valor == 6:
        print(" ---------\n",
              "| ○   ○ |\n",
              "| ○   ○ |\n",
              "| ○   ○ |\n",
              "---------\n")
        return valor

### Desenvolvimento do jogo    

print("\u001b[1m\u001b[46;1m Bem vindo ao jogo do gamão \u001b[0m\n")

print("Escolha um entre os dois jogadores para lançar primeiro o dado.\nAquele que obtiver o maior número será o primeiro jogador\n")
print("Pressione enter para a rolagem do dado:", end = '')
input()
Dado_1 = Dado()
print("Pressione enter para a rolagem do dado:", end = '')
input()
Dado_2 = Dado()

if Dado_1 > Dado_2:
    print("A primeira pessoa que jogou o dado irá iniciar o jogo com as peças amarelas\n")
elif Dado_2 > Dado_1:
    print("A segunda pessoa que jogou o dado irá iniciar o jogo com as peças amarelas\n")
else:
    print("Houve empate nos dados. Assim, a primeira pessoa que jogou o dado irá iniciar o jogo com as peças amarelas\n")

Jogador_1 = input("Jogador 1, entre com seu nome: ")
Jogador_2 = input("\nJogador 2, entre com seu nome: ")


print("\n\u001b[4mQue vença o melhor entre", Jogador_1, "e", Jogador_2, "\u001b[0m\n")

Print_Tabuleiro()

print(Jogador_1, "aperte enter para rolar os dados:", end = '')
input()

Dado_1 = random.randint(1, 6)
Dado_2 = random.randint(1, 6)

print("\nResultado dos dados: D1 =", Dado_1, "D2 =", Dado_2)

print("\nSelecione uma das opções de jogadas disponíveis abaixo:\n")
print("1 - A soma dos dados")
print("2 - Dado D1")
print("3 - Dado D2\n")

opcao = int(input("Opção: "))

if opcao == 1:
    print("1 - A soma dos dados:", Dado_1+Dado_2)
elif opcao == 2:
    print("2 - Dado D1:", Dado_1)
elif opcao == 3:
    print("3 - Dado D2:", Dado_2)
else:
    print("Valor de opção errada. Tente novamente")