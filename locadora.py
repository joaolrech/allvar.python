import os

def inptintfix():
    while True:
        try:
            inpt = int(input())
            if inpt < 0 or inpt > 2:
                raise ValueError
            return inpt
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            printmenu()

def inptintvar(quant, lista):
    while True:
        try:
            inpt = int(input())
            if inpt < 0 or inpt > quant:
                raise ValueError
            return inpt
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            listar(lista)

def inptint(desc):
    while True:
        try:
            inpt = int(input(desc))
            if inpt < 1:
                raise ValueError
            return inpt
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def printmenu():
    print('Selecione a opção desejada: ')
    print('1 - Locar veículo')
    print('2 - Devolver veículo\n')
    print('0 - SAIR\n')

def listar(lista):
    if lista:
        print('Veículos disponíveis: ' if lista == disponiveis
        else 'Veículos locados: ')
        for i, (veiculo, preco) in enumerate(lista, start = 1):
            print(f'{i} - {veiculo} - R${preco:.2f}/dia' if lista == disponiveis
            else f'{i} - {veiculo}')
    else:
        print('Nenhum veículo está disponível.' if lista == disponiveis
        else 'Nenhum veículo está locado.')
    print('\n0 - VOLTAR\n')

disponiveis = [
    ('Dolphin Mini', 87.06),
    ('Dolphin', 116.72),
    ('Dolphin Plus', 124.54),
    ('Han', 405.83),
    ('King', 124.05),
    ('Seal', 197.92),
    ('Shark', 306.42),
    ('Song Plus', 169.75),
    ('Song Pro', 133.06),
    ('Tan', 374.14),
    ('Yuan Plus', 155.51),
    ('Yuan Pro', 132.2),
]
locados = []

os.system("clear")
print('Bem vindo à locadora.py!\n')

while True:
    printmenu()
    opcao = inptintfix()
    os.system('clear')

    match opcao:
        case 1:
            listar(disponiveis)
            escolha = inptintvar(len(disponiveis), disponiveis)
            os.system("clear")
            if escolha == 0:
                continue
            veiculolocado = disponiveis[escolha - 1][0]
            print(f'{veiculolocado} locado.\n')
            locados.append(disponiveis.pop(escolha - 1))
        case 2:
            listar(locados)
            escolha = inptintvar(len(locados), locados)
            os.system("clear")
            if escolha == 0:
                continue
            veiculodevolvido = locados[escolha - 1][0]
            dias = inptint(f'Digite quantos dias você ficou com o {veiculodevolvido}: ')
            os.system("clear")
            print(f'{veiculodevolvido} devolvido.')
            print(f'Valor em haver: R${locados[escolha - 1][1] * dias:.2f}\n')
            disponiveis.append(locados.pop(escolha - 1))
        case 0:
            break

os.system("clear")
print('Programa finalizado.')