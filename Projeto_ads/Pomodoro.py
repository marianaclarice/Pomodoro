import time


menu = """
Olá! Seja Bem vindo(a) ao Projeto Pomodoro! 
Abaixo está o nosso menu <3

-----------------------------
Menu 
-----------------------------

1 - Duração 25 min x 5 min
2 - Duração 30 min x 10 min
3 - Editar
4 - Sair
"""
while True:
    print(menu)
    print(' ')

    try:
        escolha = int(input('Escolha a opção que você deseja usar no Pomodoro - Digite apenas o número: '))
    except ValueError:
        print('Digite apenas números')
        continue

    if escolha <=0 or escolha > 4:
        print('Digite um número que esteja nas opções do menu.')
        continue


    if escolha == 4:
        print('Você está saindo, até mais <3 ')
        break

#Contagem

    if escolha == 1:
        min = 25
        pausa = 5
      

    elif escolha == 2:
        min = 30
        pausa = 10

    elif escolha == 3:
        min = int(input('Digite a quantidade de minutos que você prefere: '))
        pausa = int(input('Digite quantos minutos serão a pausa: '))
        print(f'Você escolheu {min} x {pausa} minutos')
        print(' ')

#Repetição

    while True:

        print('Contagem iniciada')
        time.sleep(min * 1) #obs: mudar min e pausa para * 60, para dar os minutos.

        print('Pausa')
        time.sleep(pausa * 1)
        

    
        try:
            voltar_menu = int(input("""
            Você deseja voltar para o menu? 
                                        
            Se sim, digite 1. Se não, digite 2: 
            """))

            if voltar_menu == 1:
                print('Você está voltando para o menu :) ')
                break
            elif voltar_menu == 2:
                    continue
            elif voltar_menu <= 0 or voltar_menu > 2:
                print('Por favor, escolha 1(sim) ou 2(Não)')
                continue
        except ValueError:
            print('Digite apenas números.')
            continue

