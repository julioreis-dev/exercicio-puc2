def consultar1(valor):
    if valor % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


def consultar2(valor):
    if valor >= 0:
        return 'Positivo'
    else:
        return 'Negativo'


def consultar3(valor):
    if valor.isdigit():
        x = int(valor)
        if type(x) == int:
            return 'Inteiro'
        else:
            return 'Decimal'
    else:
        return 'erro'

number1 = input('Digite o primeiro numero? ')
number2 = input('Digite o segundo numero? ')
opt = input('Qual operação deseja realizar?\nA - Par ou impar.\nB - Positivo ou negativo.\nC - Inteiro ou decimal.')
lista_opt = ['a', 'b', 'c']
if opt.lower() in lista_opt:
    if opt == 'a':
        resutado1 = consultar1(number1)
        print('O primeiro numero é:', resutado1)
        resutado2 = consultar1(number2)
        print('O segundo numero é:', resutado2)
    elif opt == 'b':
        resutado1 = consultar2(number1)
        print('O primeiro numero é:', resutado1)
        resutado2 = consultar2(number2)
        print('O segundo numero é:', resutado2)
    elif opt == 'c':
        resutado1 = consultar3(number1)
        print('O primeiro numero é:', resutado1)
        resutado2 = consultar3(number2)
        print('O segundo numero é:', resutado2)
