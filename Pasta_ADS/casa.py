cont = 0
soma = 0
maior = None
menor = None

while True:
    num = int(input('Digite um número inteiro. se quiser sair, digite 0: '))
    if num == 0:
        break
    if num < 0:
        print('Número negativo ignorado.')
        continue

    soma += num
    cont += 1
    
if cont > 0:
    media = soma / cont
    print(f'Total de números digitados: {cont}')
    print(f'Soma dos números: {soma}')
    print(f'Média dos números: {media:.2f}')
else:
    print('Nenhum número foi digitado.')

