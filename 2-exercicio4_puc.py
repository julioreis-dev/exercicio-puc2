def descontar(value):
    desc_total = value*0.10
    preco_final = value-desc_total
    return preco_final


def precificar_morango():
    quant = int(input('Quantos kilos deseja comprar? '))
    preco = 3.5
    preco1 = 3.2
    if quant <= 5:
        tarifa = (preco*quant)
        if tarifa > 25:
            tarifa1 = descontar(tarifa)
            return tarifa1
        else:
            return tarifa
    elif 5 < quant <= 8:
        tarifa = (preco1*quant)
        if tarifa > 25:
            tarifa1 = descontar(tarifa)
            return tarifa1
        else:
            return tarifa
    elif quant > 8:
        desc = (preco1*quant)*0.10
        tarifa = (preco1*quant)-desc
        return tarifa


def precificar_maca():
    quant = int(input('Quantos kilos deseja comprar? '))
    preco = 2.8
    preco1 = 2.5
    if quant <= 5:
        tarifa = (preco * quant)
        if tarifa > 25:
            tarifa1 = descontar(tarifa)
            return tarifa1
        else:
            return tarifa
    elif 5 < quant <= 8:
        tarifa = (preco1 * quant)
        if tarifa > 25:
            tarifa1 = descontar(tarifa)
            return tarifa1
        else:
            return tarifa
    elif quant > 8:
        desc = (preco1 * quant) * 0.10
        tarifa = (preco1 * quant) - desc
        return tarifa


tipo = input('Que tipo de fruta?\nM-Morango\nN-Maçã')
lista_tipo = ['m', 'n']
if tipo.lower() in lista_tipo:
    if tipo == 'm':
        valor = precificar_morango()
        print('O valor final é de: R$ ', round(valor, 2))
    elif tipo == 'n':
        valor1 = precificar_maca()
        print('O valor final é de: R$ ', round(valor1, 2))
