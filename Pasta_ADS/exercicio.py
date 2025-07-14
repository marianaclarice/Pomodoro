cont = 1
soma = 0
valores = []

while cont <= 10:
    num = int(input(f'Digite o {cont}º número: '))
    if num > 0:
        soma += num
        cont += 1
        valores.append(num)
    else:
        print('Escreva apenas números positivos.')

media = soma / 10
print('   ')
print(f'Os valores digitados foram: {valores}')
print(f'A soma total dos valores é: {soma:.2f}')
print(f'A média dos valores é: {media:.2f}')