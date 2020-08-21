def precificar_alcool():
    quant = int(input('Quantos litros deseja abastecer? '))
    if quant <= 20:
        desc = (1.9*quant)*0.03
        tarifa = (1.9*quant)-desc
        return tarifa
    else:
        desc = (1.9*quant)*0.05
        tarifa = (1.9 * quant) - desc
        return tarifa


def precificar_gasolina():
    quant = int(input('Quantos litros deseja abastecer? '))
    if quant <= 20:
        desc = (2.5 * quant) * 0.04
        tarifa = (2.5 * quant) - desc
        return tarifa
    else:
        desc = (2.5 * quant) * 0.06
        tarifa = (2.5 * quant) - desc
        return tarifa


tipo = input('Que tipo de combustível?\nA-alcool\nG-gasolina')
lista_tipo = ['a', 'g']
if tipo.lower() in lista_tipo:
    if tipo == 'a':
        valor = precificar_alcool()
        print('O valor final é de: R$ ', round(valor, 2))
    elif tipo == 'g':
        valor1 = precificar_gasolina()
        print('O valor final é de: R$ ', round(valor1, 2))
