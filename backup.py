import os

def inptintfix():
    while True:
        try:
            inp = int(input())
            if inp < 0 or inp > 2:
                raise ValueError
            return inp
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            printmenu()

def inptintvar(quant, lista):
    while True:
        try:
            inp = int(input())
            if inp < 0 or inp > quant:
                raise ValueError
            return inp
        except ValueError:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            listar(lista)

def inptint(desc):
    while True:
        try:
            inp = int(input(desc))
            if inp < 1:
                raise ValueError
            return inp
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def printmenu():
    print('Selecione a opção desejada: ')
    print('1 - Locar veículo')
    print('2 - Devolver veículo \n')
    print('0 - SAIR \n')

def listar(lista):
    if lista == disponiveis:
        print('Veículos disponíveis:')
        for i, (veiculo, preco) in enumerate(disponiveis.items(), start = 1):
            print(f'{i} - {veiculo} - R${preco:.2f}/dia')
    if lista == locados:
        if locados:
            print('Veículos locados:')
            for i, veiculo in enumerate(locados, start = 1):
                print(f'{i} - {veiculo}')
        else:
            print('Nenhum veículo está locado.')
    print('\n0 - VOLTAR \n')

disponiveis = {
    'Dolphin Mini' : 87.06,
    'Dolphin' : 116.72,
    'Dolphin Plus' : 124.54,
    'Han' : 405.83,
    'King' : 124.05,
    'Seal' : 197.92,
    'Shark' : 306.42,
    'Song Plus' : 169.75,
    'Song Pro' : 133.06,
    'Tan' : 374.14,
    'Yuan Plus' : 155.51,
    'Yuan Pro' : 132.2,
    }
locados = {}

os.system("clear")
print('Bem vindo à locadora.py! \n')

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
            veiculolocado = list(disponiveis.keys())[escolha - 1]
            print(f'{veiculolocado} locado. \n')
            locados[veiculolocado] = disponiveis.pop(veiculolocado)
        case 2:
            listar(locados)
            escolha = inptintvar(len(locados), locados)
            os.system("clear")
            if escolha == 0:
                continue
            veiculodevolvido = list(locados.keys())[escolha - 1]
            dias = inptint(f'Digite quantos dias você ficou com o {veiculodevolvido}: ')
            os.system("clear")
            print(f'{veiculodevolvido} devolvido.')
            print(f'Valor em haver: R${locados[veiculodevolvido] * dias:.2f} \n')
            disponiveis[veiculodevolvido] = locados.pop(veiculodevolvido)
        case 0:
            break

os.system("clear")
print('Programa finalizado.')