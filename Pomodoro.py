menu = """
-----------------------------
Menu 
-----------------------------

1 - Duração 25 min x 5 min
2 - Duração 30 min x 10 min
3 - Editar
4 - Sair
"""
print(menu)
print(' ')

try:
    escolha = int(input('Escolha a opção que você deseja usar no Pomodoro - Digite apenas o número: '))
except ValueError:
    print('Digite apenas números')
    exit()


import time

if escolha <=0 or escolha > 4:
    print('Digite um número que esteja nas opções do menu.')
if escolha == 1:
    print('Contagem iniciada')
    time.sleep(5)
    print('Pausa')
    time.sleep(5)

elif escolha == 2:
    print('Contagem iniciada')
    time.sleep(5)
    print('Pausa')
    time.sleep(5)

elif escolha == 3:
    min = int(input('Digite a quantidade de minutos que você prefere: '))
    pausa = int(input('Digite quantos minutos serão a pausa: '))
    print(f'Você escolheu {min} x {pausa} minutos')
    print(' ')

    minutos_contagem = min * 1
    pausa_contagem = pausa * 1

    print('Iniciando contagem')
    time.sleep(minutos_contagem)
    print('Pausa')
    time.sleep(pausa_contagem)



else:
    print('Você está saindo, até mais <3')


    