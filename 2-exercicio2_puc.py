def answear(resp):
    if resp.lower() == 's':
        return 1
    else:
        return 0


def analitcs(lista):
    sun_answ = lista.count(1)
    lista_possib = ['inocente', 'inocente', 'Suspeita', 'Cúmplice', 'Cúmplice', 'Assassino']
    return lista_possib[sun_answ]


lista_anw = []
arg = True
n = 0
while arg:
    lista_question = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ',
                  'Possuia dívidas com a vítima? ', 'Já trabalhou com a vítima? ']
    question = input(lista_question[n])
    lista_resp = ['s', 'n']
    if question in lista_resp:
        if question.lower() == 's':
            lista_anw.append(1)
            n = n + 1
        else:
            lista_anw.append(0)
            n = n + 1
    else:
        print('Try again, Please!!!')
    if n == 5:
        arg = False
final = analitcs(lista_anw)
print(final)
