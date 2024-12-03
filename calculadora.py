import os

def inptfloat(desc):
    while True:
        try:
            return float(input(desc))
        except ValueError:
            print('Entrada inválida. Tente novamente.')

def inptmenu():
    while True:
        inpt = input().upper()
        if inpt not in ['+', '-', '*', '/', 'X']:
            os.system("clear")
            print('Entrada inválida. Tente novamente.\n')
            printmenu()
        else:
            return inpt

def printmenu():
    print('Selecione a operação desejada: ')
    print('+ Adição')
    print('- Subtração')
    print('* Multiplicação')
    print('/ Divisão \n')
    print('X SAIR \n')

def entrada(titulo):
    print(f'{titulo} \n')
    x = inptfloat('Digite o 1º termo da operação: ')
    y = inptfloat('Digite o 2º termo da operação: ')
    os.system("clear")
    return x, y

os.system("clear")
print('Bem vindo à calculadora.py! \n')

while True:
    printmenu()
    operacao = inptmenu()
    os.system("clear")

    match operacao:
        case '+':
            x, y = entrada('SOMA')
            z = x + y
        case '-':
            x, y = entrada('SUBTRAÇÃO')
            z = x - y
        case '*':
            x, y = entrada('MULTIPLICAÇÃO')
            z = x * y
        case '/':
            x, y = entrada('DIVISÃO')
            if y == 0:
                print('Impossível dividir por 0. \n')
            else:
                z = x / y
        case 'X':
            break

    print(f'{x:g} {operacao} {y:g} = {z:g} \n')

os.system("clear")
print('Programa finalizado.')