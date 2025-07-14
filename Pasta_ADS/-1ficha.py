# i = índice da linha, j = índice da coluna

linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

matriz = []

i = 0
while i < linhas:
    lista_linha = []
    j = 0
    while j < colunas:
        if i < j:
           operacao =  2*i + 7*j + 2
        elif i == j:
            operacao = 3 * i**2 + 1
        elif i > j:
           operacao = 4 * i**3 + 5*j**2
        lista_linha.append(operacao)
        j = j + 1
    matriz.append(lista_linha)
    i = i + 1

print(' ')
print('A matriz é: ')
for linha in matriz:
    print(linha)


