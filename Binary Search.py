# Criar e coletar em um vetor [20] com números aleatórios de 0 a 100. Classificar este vetor em ordem crescente e
# mostre os dados.' Programador: Hugo Leça Ribeiro Data de Elaboração: 13.11.2019

import random


def carrega(vt):
    for i in range(0, 20, 1):
        vt.append(random.randint(0, 100))
    return (vt)


def classifica(vt):
    for i in range(0, 19, 1):
        for j in range((i + 1), 20, 1):
            if vt[i] > vt[j]:
                vt[i], vt[j] = vt[j], vt[i]
    return (vt)


def pesquisa(vt):
    n = int(input("\nDigite aqui um número que queira pesquisar: "))
    tentativas = 0
    achei = False
    minindex = 0
    maxindex = (len(vt) - 1)
    media = 0
    while minindex != maxindex and achei == False:
        tentativas = tentativas + 1
        media = ((maxindex + minindex) // 2)
        if n == vt[media]:
            achei = True
        else:
            if n > vt[media]:
                minindex = (media) + 1
            if n < vt[media]:
                maxindex = (media) - 1
    if (achei == True):
        print("O número", n, "está localizado na posição", (media), "e usamos", tentativas, "tentativas")
    else:
        tentativas = tentativas + 1
        if n == vt[minindex]:
            print("O número", n, "está localizado na posição", (minindex), "e usamos", tentativas,
                  "tentativas para encontrá-lo")
        else:
            print("O número", n, "não está nessa lista e usamos", tentativas, "tentativas para verificar.")


vt = []
carrega(vt)
print(f'O vetor gerado é este: \n{vt}')
classifica(vt)
print(f'\nEste é o vetor já ordenado: \n{vt}')
pesquisa(vt)