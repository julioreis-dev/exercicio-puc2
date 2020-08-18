def analisar(med):
    lista_grau = [(10.0, 9.0, 'A', 'Aprovado'), (9.0, 7.5, 'B', 'Aprovado'), (7.5, 6.0, 'C', 'Aprovado'),
                  (6.0, 4.0, 'D', 'Reprovado'), (4.0, 0.0, 'E', 'Reprovado')]
    for secao in lista_grau:
        if secao[0] > med >= secao[1]:
            return secao[2], secao[3]


nota1 = float(input('Digite a primeira nota? '))
nota2 = float(input('Digite a segunda nota? '))
media = round((nota1 + nota2)/2, 2)
x = analisar(media)
print('O aluno teve media {},alcançando o conceito {}'.format(media, x[0]))
print('Status:', x[1])
